
import 'dart:io';
import 'dart:typed_data';

import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:gallery_app_flutter/ImageEntry.dart';
import 'package:image_picker/image_picker.dart';

class AddImageEntryPage extends StatefulWidget {

  @override
  State<StatefulWidget> createState() =>
      _ImageEntryState<AddImageEntryPage>();

}

class UpdateImageEntryPage extends StatefulWidget {

  UpdateImageEntryPage(this.entry);

  final ImageEntry entry;

  @override
  State<StatefulWidget> createState() =>
      _ImageEntryState(entry: entry);

}

class _ImageEntryState<T extends StatefulWidget> extends State<T> {
  _ImageEntryState({
    ImageEntry entry
  }) {
    if (entry != null) {
      _title = entry.title;
      _description = entry.description;
      _tags = entry.tags.join(" ");
      _bytes = entry.image;
      _entry = entry;
    }
  }
  ImageEntry _entry;
  String _title, _description, _tags;
  PickedFile _image;
  ImagePicker _picker = ImagePicker();
  Uint8List _bytes;

  @override
  void initState() {
    super.initState();
  }

  @override
  void dispose() {
    super.dispose();
  }
  
  _openGallery() async {
    PickedFile image = await _picker.getImage(source: ImageSource.gallery);

    setState(() {
      _image = image;
    });
  }

  _showSnackBar(BuildContext context, String text) {
    Scaffold.of(context).showSnackBar(SnackBar(
      content: Text(text),
      duration: Duration(milliseconds: 1500),
    ));
    return false;
  }

  _validateInputs(BuildContext context) {
    if (_title == null || _title.trim().isEmpty) return _showSnackBar(context, "Title cannot be empty");
    if (_description == null || _description.trim().isEmpty) return _showSnackBar(context, "Description cannot be empty");
    if (_tags == null || _tags.trim().isEmpty) return _showSnackBar(context, "Tags cannot be empty");
    if (_image == null && _entry == null) return _showSnackBar(context, "You must upload an image");
    return true;
  }

  VoidCallback _save(BuildContext context) => () async {
    if (_validateInputs(context)) {
      var entity = ImageEntry(
          title: _title,
          description: _description,
          tags: _tags.split(new RegExp(r"\s")),
          image: _entry == null || _image != null ? await _image.readAsBytes() : _bytes
      );
      if (_entry != null) {
        entity.id = _entry.id;
      }
      Navigator.pop(context, entity);
    }
  };

  Image _buildImage() => _image != null ?
    Image.file(
      File(_image.path),
      fit: BoxFit.fitWidth,
      width: MediaQuery.of(context).size.width
    ) : _bytes != null ? Image.memory(
      _bytes, fit:
      BoxFit.fitWidth,
      width: MediaQuery.of(context).size.width,
    ) : Image.network(
      'https://breakthrough.org/wp-content/uploads/2018/10/default-placeholder-image.png',
      fit: BoxFit.fitWidth,
      width: MediaQuery.of(context).size.width,
    );

  @override
  Widget build(BuildContext context) => GestureDetector(
    onTap: () {
      FocusScopeNode currentFocus = FocusScope.of(context);
      if (!currentFocus.hasPrimaryFocus) {
        currentFocus.unfocus();
      }
    },
    child: Scaffold(
        appBar: AppBar(
          title: Text("Add an image entry"),
        ),
        floatingActionButton: Builder(builder: (BuildContext context) =>
            FloatingActionButton.extended(
              onPressed: _save(context),
              label: Text('SAVE TO GALLERY'),
            ),
        ),
        body: SingleChildScrollView(
          padding: EdgeInsets.only(bottom: 75.0),
          child: Column(
            mainAxisAlignment: MainAxisAlignment.start,
            children: <Widget>[
              GestureDetector(
                child: _buildImage(),
                onTap: _openGallery,
              ),
              TextButton(
                  onPressed: _openGallery,
                  child: Text("UPLOAD IMAGE")
              ),
              Padding(
                padding: EdgeInsets.all(10.0),
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: <Widget>[
                    _outlinedTextField(
                      label: "Title",
                      initialValue: _title,
                      onChanged: (value) => setState(() {
                        _title = value;
                      }),
                    ),
                    _outlinedTextField(
                      label: 'Description',
                      initialValue: _description,
                      onChanged: (value) => setState(() {
                        _description = value;
                      }),
                    ),
                    _outlinedTextField(
                        label: 'Tags (separated by space)',
                        initialValue: _tags,
                        onChanged: (value) => setState(() {
                          _tags = value;
                        })
                    ),
                  ],
                ),
              ),
            ],
          ),
        )
    ),
  );
}

Widget _outlinedTextField({
  @required void Function(String) onChanged,
  @required String label,
  String initialValue
}) => Padding(
    padding: EdgeInsets.only(top: 10.0),
    child: TextFormField(
      initialValue: initialValue,
      onChanged: onChanged,
      decoration: InputDecoration(
        labelText: label,
        border: OutlineInputBorder(),
      ),
    )
);