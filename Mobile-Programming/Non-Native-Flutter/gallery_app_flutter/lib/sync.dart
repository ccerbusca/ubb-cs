import 'dart:async';

import 'package:dio/dio.dart';
import 'package:gallery_app_flutter/ImageEntry.dart';
import 'package:gallery_app_flutter/environment.dart';
import 'package:retrofit/http.dart';
import 'package:retrofit/http.dart' as h;
import 'package:sqflite/sqflite.dart';
import 'package:path/path.dart';


part 'sync.g.dart';

class ImageEntrySynchronizer {


  static final ImageEntrySynchronizer _instance = ImageEntrySynchronizer._internal();
  factory ImageEntrySynchronizer() => _instance;

  ImageEntrySynchronizer._internal() {
    _dio = Dio(BaseOptions(
      baseUrl: apiBaseUrl,
      connectTimeout: 5000,
      receiveTimeout: 5000,
    ));
    restClient = RestClient(_dio);

  }

  Dio _dio;
  RestClient restClient;
}


@RestApi()
abstract class RestClient {

  factory RestClient(Dio dio, {String baseUrl}) = _RestClient;

  @POST("/imageEntry")
  Future<void> save(@Body() ImageEntry entry);

  @PATCH("/imageEntry")
  Future<void> update(@Body() ImageEntry entry);

  @DELETE("/imageEntry/{id}")
  Future<void> delete(@Path() String id);

  @GET("/imageEntry")
  Future<List<ImageEntry>> getAll();

  @POST("/imageEntry/batch")
  Future<void> batchAdd(@Body() List<ImageEntry> entries);

  @POST("/imageEntry/batch/delete")
  Future<void> batchDelete(@Body() List<String> ids);

  @PATCH("/imageEntry/batch")
  Future<void> batchUpdate(@Body() List<ImageEntry> entries);

}