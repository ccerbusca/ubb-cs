import 'dart:typed_data';

import 'package:flutter/cupertino.dart';
import 'package:uuid/uuid.dart';

class ImageEntry {
  static Uuid generator = Uuid();

  ImageEntry({
    @required this.title,
    @required this.description,
    @required this.tags,
    @required this.image,
    this.dateAdded,
    this.id
  }) : assert(title != null),
        assert(description != null),
        assert(tags != null && tags.length > 0),
        assert(image != null) {
    this.dateAdded ??= DateTime.now();
    this.id ??= generator.v4();
  }

  final String title;
  final String description;
  final List<String> tags;
  final Uint8List image;
  DateTime dateAdded;
  String id;

  @override
  bool operator ==(Object other) {
    if (other == null) return false;

    return other is ImageEntry && other.id == this.id;
  }

  @override
  int get hashCode => id.hashCode;

}
