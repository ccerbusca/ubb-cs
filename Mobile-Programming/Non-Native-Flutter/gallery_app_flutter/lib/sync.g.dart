// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'sync.dart';

// **************************************************************************
// RetrofitGenerator
// **************************************************************************

class _RestClient implements RestClient {
  _RestClient(this._dio, {this.baseUrl}) {
    ArgumentError.checkNotNull(_dio, '_dio');
  }

  final Dio _dio;

  String baseUrl;

  @override
  Future<void> save(entry) async {
    ArgumentError.checkNotNull(entry, 'entry');
    const _extra = <String, dynamic>{};
    final queryParameters = <String, dynamic>{};
    final _data = <String, dynamic>{};
    _data.addAll(entry?.toJson() ?? <String, dynamic>{});
    _data.removeWhere((k, v) => v == null);
    await _dio.request<void>('/imageEntry',
        queryParameters: queryParameters,
        options: RequestOptions(
            method: 'POST',
            headers: <String, dynamic>{},
            extra: _extra,
            baseUrl: baseUrl),
        data: _data);
    return null;
  }

  @override
  Future<void> update(entry) async {
    ArgumentError.checkNotNull(entry, 'entry');
    const _extra = <String, dynamic>{};
    final queryParameters = <String, dynamic>{};
    final _data = <String, dynamic>{};
    _data.addAll(entry?.toJson() ?? <String, dynamic>{});
    _data.removeWhere((k, v) => v == null);
    await _dio.request<void>('/imageEntry',
        queryParameters: queryParameters,
        options: RequestOptions(
            method: 'PATCH',
            headers: <String, dynamic>{},
            extra: _extra,
            baseUrl: baseUrl),
        data: _data);
    return null;
  }

  @override
  Future<void> delete(id) async {
    ArgumentError.checkNotNull(id, 'id');
    const _extra = <String, dynamic>{};
    final queryParameters = <String, dynamic>{};
    final _data = <String, dynamic>{};
    await _dio.request<void>('/imageEntry/$id',
        queryParameters: queryParameters,
        options: RequestOptions(
            method: 'DELETE',
            headers: <String, dynamic>{},
            extra: _extra,
            baseUrl: baseUrl),
        data: _data);
    return null;
  }

  @override
  Future<List<ImageEntry>> getAll() async {
    const _extra = <String, dynamic>{};
    final queryParameters = <String, dynamic>{};
    final _data = <String, dynamic>{};
    final _result = await _dio.request<List<dynamic>>('/imageEntry',
        queryParameters: queryParameters,
        options: RequestOptions(
            method: 'GET',
            headers: <String, dynamic>{},
            extra: _extra,
            baseUrl: baseUrl),
        data: _data);
    var value = _result.data
        .map((dynamic i) => ImageEntry.fromJson(i as Map<String, dynamic>))
        .toList();
    return value;
  }

  @override
  Future<void> batchAdd(entries) async {
    ArgumentError.checkNotNull(entries, 'entries');
    const _extra = <String, dynamic>{};
    final queryParameters = <String, dynamic>{};
    final _data = entries.map((e) => e.toJson()).toList();
    await _dio.request<void>('/imageEntry/batch',
        queryParameters: queryParameters,
        options: RequestOptions(
            method: 'POST',
            headers: <String, dynamic>{},
            extra: _extra,
            baseUrl: baseUrl),
        data: _data);
    return null;
  }

  @override
  Future<void> batchDelete(ids) async {
    ArgumentError.checkNotNull(ids, 'ids');
    const _extra = <String, dynamic>{};
    final queryParameters = <String, dynamic>{};
    final _data = ids;
    await _dio.request<void>('/imageEntry/batch/delete',
        queryParameters: queryParameters,
        options: RequestOptions(
            method: 'POST',
            headers: <String, dynamic>{},
            extra: _extra,
            baseUrl: baseUrl),
        data: _data);
    return null;
  }

  @override
  Future<void> batchUpdate(entries) async {
    ArgumentError.checkNotNull(entries, 'entries');
    const _extra = <String, dynamic>{};
    final queryParameters = <String, dynamic>{};
    final _data = entries.map((e) => e.toJson()).toList();
    await _dio.request<void>('/imageEntry/batch',
        queryParameters: queryParameters,
        options: RequestOptions(
            method: 'PATCH',
            headers: <String, dynamic>{},
            extra: _extra,
            baseUrl: baseUrl),
        data: _data);
    return null;
  }
}
