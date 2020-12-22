import 'dart:convert';
import 'dart:typed_data';

import 'package:connectivity/connectivity.dart';
import 'package:gallery_app_flutter/sync.dart';
import 'package:gallery_app_flutter/utils.dart';
import 'package:json_annotation/json_annotation.dart';
import 'package:flutter/cupertino.dart';
import 'package:retrofit/retrofit.dart';
import 'package:uuid/uuid.dart';
import 'package:sqflite/sqflite.dart';
import 'package:path/path.dart';

part 'ImageEntry.g.dart';


final String tableImageEntry = 'image_entries';
final String columnUuid = 'uuid';
final String columnTitle = 'title';
final String columnDesc = 'desc';
final String columnImage = 'image';
final String columnTags = 'tags';
final String columnDateAdded = 'dateAdded';


final String batchItemId = 'id';
final String batchDeleteTable = 'batch_delete';
final String batchAddTable = 'batch_add';

@JsonSerializable()
class ImageEntry {
  static Uuid generator = Uuid();


  ImageEntry({
    @required this.title,
    @required this.description,
    @required this.tags,
    @required this.image,
    this.id
  }) : assert(title != null),
        assert(description != null),
        assert(tags != null && tags.length > 0),
        assert(image != null) {
    this.id ??= generator.v4();
  }

  final String title;
  final String description;
  final List<String> tags;

  @_ByteArrayConverter() final Uint8List image;
  @JsonKey(name: "uuid") String id;

  @override
  bool operator ==(Object other) {
    if (other == null) return false;

    return other is ImageEntry && other.id == this.id;
  }

  @override
  int get hashCode => id.hashCode;

  Map<String, dynamic> toMap() => <String, dynamic> {
      columnUuid: id,
      columnTitle: title,
      columnDesc: description,
      columnImage: image,
      columnTags: tags.join(',')
    };

  factory ImageEntry.fromMap(Map<String, dynamic> map) {
    return ImageEntry(
        id: map[columnUuid],
        title: map[columnTitle],
        description: map[columnDesc],
        tags: map[columnTags].split(','),
        image: map[columnImage]
    );
  }

  factory ImageEntry.fromJson(Map<String, dynamic> json) => _$ImageEntryFromJson(json);

  Map<String, dynamic> toJson() => _$ImageEntryToJson(this);

}

class _ByteArrayConverter implements JsonConverter<Uint8List, Object> {
  const _ByteArrayConverter();

  @override
  Uint8List fromJson(Object json) {
    return Utils.base64Decoder.convert(json.toString());
  }

  @override
  Object toJson(Uint8List object) {
    return Utils.base64Encoder.convert(object);
  }
  
}

class ImageEntryProvider {

  bool _hasInternetConnection;

  ImageEntryProvider._internal() {
    initConnectivityListener();
  }

  static final ImageEntryProvider _instance = ImageEntryProvider._internal();

  factory ImageEntryProvider() {
    return _instance;
  }

  Database db;
  ImageEntrySynchronizer synchronizer = ImageEntrySynchronizer();


  Future open(String dbName) async {
    var dbPath = await getDatabasesPath();
    var path = join(dbPath, dbName);
    db = await openDatabase(path, version: 4,
      onCreate: (Database db, int version) async {
        await db.execute('''
          create table $tableImageEntry (
            $columnUuid text primary key,
            $columnTitle text not null,
            $columnDesc text not null,
            $columnImage blob not null,
            $columnTags text not null
          )'''
        );
        await _createBatchTable(db, batchDeleteTable);
        await _createBatchTable(db, batchAddTable);
      });
  }

  Future<void> _createBatchTable(Database db, String tableName) async {
    await db.execute('''
          create table $tableName (
            $batchItemId integer primary key autoincrement,
            $columnUuid text not null
          )'''
    );
  }

  void initConnectivityListener() async {
    var res = await Connectivity().checkConnectivity();
    _hasInternetConnection = res == ConnectivityResult.wifi || res == ConnectivityResult.mobile;

    Connectivity().onConnectivityChanged.listen((event) {
      _hasInternetConnection = event == ConnectivityResult.wifi || event == ConnectivityResult.mobile;
    });
  }

  Future<ImageEntry> insert(ImageEntry imageEntry) async {
    await db.insert(tableImageEntry, imageEntry.toMap());
    if (_hasInternetConnection) {
      await synchronizer.restClient.save(imageEntry);
    } else {
      await db.insert(batchAddTable, {
        columnUuid: imageEntry.id
      });
    }
    return imageEntry;
  }

  Future<List<ImageEntry>> getAll() async {
    List<Map> maps = await db.query(tableImageEntry,
        columns: [columnUuid, columnTitle, columnDesc, columnImage, columnTags]
    );
    return maps.map((e) => ImageEntry.fromMap(e)).toList();
  }

  Future<ImageEntry> get(String uuid) async {
    List<Map> maps = await db.query(tableImageEntry,
        columns: [columnUuid, columnTitle, columnDesc, columnImage, columnTags],
        where: '$columnUuid = ?',
        whereArgs: [uuid]
    );
    if (maps.length > 0) {
      return ImageEntry.fromMap(maps.first);
    }
    return null;
  }

  Future<void> delete(String id) async {
    await db.delete(tableImageEntry, where: '$columnUuid = ?', whereArgs: [id]);
    if (_hasInternetConnection) {
      await synchronizer.restClient.delete(id).catchError((e) => print(e));
    } else {
      await db.delete(batchAddTable, where: '$columnUuid = ?', whereArgs: [id]);
      await db.insert(batchDeleteTable, {
        columnUuid: id
      });
    }
  }

  Future<bool> exists(String table, String column, String value) async {
    List<Map> map = await db.query(table, where: '$column = ?', whereArgs: [value]);
    return map.length != 0;
  }

  Future<void> update(ImageEntry entry) async {
    await db.update(tableImageEntry, entry.toMap(),
      where: '$columnUuid = ?', whereArgs: [entry.id]
    );
    if (_hasInternetConnection) {
      synchronizer.restClient.save(entry);
    } else {
      if (!await exists(batchAddTable, columnUuid, entry.id)) {
        await db.insert(batchAddTable, {
          columnUuid: entry.id
        });
      }
    }
  }

  Future close() async => db.close();



  Future<void> batchDelete() async {
    List<Map> maps = await db.query(batchDeleteTable,
        columns: [columnUuid]
    );
    synchronizer.restClient
        .batchDelete(maps.map((e) => e[columnUuid]).toList());
  }

  Future<void> batchAdd() async {

    List<Map> maps = await db.rawQuery('''
      select ie.$columnUuid, ie.$columnTitle, ie.$columnDesc, ie.$columnImage, ie.$columnTags
      from $tableImageEntry ie inner join $batchAddTable ba on ie.$columnUuid = ba.$columnUuid
    ''');
    synchronizer.restClient
        .batchAdd(maps.map((e) => ImageEntry.fromMap(e)).toList());
  }

  // Future<void> batchUpdate() async {
  //
  //   List<Map> maps = await db.rawQuery('''
  //     select ie.$columnUuid, ie.$columnTitle, ie.$columnDesc, ie.$columnImage, ie.$columnTags
  //     from $tableImageEntry ie inner join $batchUpdateTable ba on ie.$columnUuid = ba.$columnUuid
  //   ''');
  //   synchronizer.restClient
  //       .batchUpdate(maps.map((e) => ImageEntry.fromMap(e)).toList());
  // }

}
