// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'ImageEntry.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

ImageEntry _$ImageEntryFromJson(Map<String, dynamic> json) {
  return ImageEntry(
    title: json['title'] as String,
    description: json['description'] as String,
    tags: (json['tags'] as List)?.map((e) => e as String)?.toList(),
    image: const _ByteArrayConverter().fromJson(json['image']),
    id: json['uuid'] as String,
  );
}

Map<String, dynamic> _$ImageEntryToJson(ImageEntry instance) =>
    <String, dynamic>{
      'title': instance.title,
      'description': instance.description,
      'tags': instance.tags,
      'image': const _ByteArrayConverter().toJson(instance.image),
      'uuid': instance.id,
    };
