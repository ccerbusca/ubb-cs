
import 'dart:typed_data';

import 'package:flutter/cupertino.dart';
import 'package:flutter/foundation.dart';
import 'package:flutter/material.dart';
import 'package:gallery_app_flutter/AddUpdateImageEntryPage.dart';
import 'CardItem.dart';
import 'ImageEntry.dart';



class ImageEntriesList extends StatefulWidget {
  @override
  _ImageEntriesListState createState() =>
      _ImageEntriesListState();

}

class _ImageEntriesListState extends State<ImageEntriesList> {

  final GlobalKey<AnimatedListState> _listKey =
      GlobalKey<AnimatedListState>();
  ListModel<ImageEntry> _list;

  @override
  void initState() {
    super.initState();
    _list = ListModel<ImageEntry>(
      listKey: _listKey,
      initialItems: <ImageEntry>[],
      removedItemBuilder: _buildRemovedItem,
    );
  }

  Widget _buildItem(BuildContext context, int index, Animation<double> animation) {
    return CardItem(
      animation: animation,
      item: _list[index],
      onDelete: _deleteItemHandler(_list[index]),
      onEdit: _editItemHandler(_list[index]),
    );
  }

  Widget _buildRemovedItem(
      ImageEntry item, BuildContext context, Animation<double> animation) {
    return CardItem(
      animation: animation,
      item: item,
      onDelete: _deleteItemHandler(item),
      onEdit: _editItemHandler(item),
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Gallery'),
      ),
      body: AnimatedList(
        key: _listKey,
        initialItemCount: _list.length,
        itemBuilder: _buildItem,
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: _navigateToAddPageAndAddEntry,
        child: Icon(Icons.add),
        backgroundColor: Theme.of(context).primaryColor,
      ),
    );
  }

  _deleteItemHandler(ImageEntry entry) => () {
    _list.removeAt(_list.indexOf(entry));
  };

  _editItemHandler(ImageEntry entry) => () async {

    final result = await Navigator.push(
        context,
        MaterialPageRoute(builder: (context) => UpdateImageEntryPage(entry))
    );
    if (result != null)
      _list.update(entry, result);
  };

  _navigateToAddPageAndAddEntry() async {
    final result = await Navigator.push(
        context,
        MaterialPageRoute(builder: (context) => AddImageEntryPage())
    );

    if (result != null)
      _list.add(result);
  }

}

class ListModel<T> {
  ListModel({
    @required this.listKey,
    @required this.removedItemBuilder,
    Iterable<T> initialItems,
  }) : assert(listKey != null),
       assert(removedItemBuilder != null),
       _items = List<T>.from(initialItems ?? <T>[]);

  final GlobalKey<AnimatedListState> listKey;
  final dynamic removedItemBuilder;
  final List<T> _items;

  AnimatedListState get _animatedList => listKey.currentState;

  void insertAtIndex(int index, T item) {
    _items.insert(index, item);
    _animatedList.insertItem(index);
  }

  void add(T item) {
    _items.add(item);
    _animatedList.insertItem(_items.length - 1);
  }

  void update(T old, T newI) {
    var index = _items.indexOf(old);
    _items[index] = newI;
    // _items.replaceRange(0, _items.length,
    //     _items.map((item) => item == old ? newI : old)
    // );
  }

  T removeAt(int index) {
    final T removed = _items.removeAt(index);
    if (removed != null) {
      _animatedList.removeItem(index, (context, animation) =>
                  removedItemBuilder(removed, context, animation)
      );
    }
    return removed;
  }

  int get length => _items.length;

  T operator [](int index) => _items[index];

  int indexOf(T item) => _items.indexOf(item);
}