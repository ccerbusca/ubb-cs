import 'package:flutter/material.dart';
import 'package:gallery_app_flutter/ImageEntriesList.dart';
import 'package:gallery_app_flutter/environment.dart';

void main() {
  setEnv(Environment.dev);
  runApp(MaterialApp(
    title: "Gallery",
    home: ImageEntriesList(),
    theme: ThemeData(
      primarySwatch: Colors.deepPurple,
      visualDensity: VisualDensity.adaptivePlatformDensity
    ),
  ));
}
