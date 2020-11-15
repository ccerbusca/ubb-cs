import 'package:flutter/material.dart';
import 'ImageEntry.dart';

class CardItem extends StatelessWidget {
  const CardItem({
    Key key,
    @required this.animation,
    @required this.onEdit,
    @required this.onDelete,
    @required this.item
  }) : assert(animation != null),
        assert(item != null),
        super(key: key);

  final Animation<double> animation;
  final VoidCallback onEdit;
  final VoidCallback onDelete;
  final ImageEntry item;

  @override
  Widget build(BuildContext context) {
    return SizeTransition(
      axis: Axis.vertical,
      sizeFactor: animation,
      child: GestureDetector(
          behavior: HitTestBehavior.opaque,
          onLongPress: (){
            Scaffold.of(context).showSnackBar(SnackBar(content: Text('123'), duration: Duration(milliseconds: 1500)));
          },
          child: Card(
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.stretch,
                children: <Widget>[
                  Image.memory(
                    item.image,
                    fit: BoxFit.fitWidth,
                    width: MediaQuery.of(context).size.width,
                  ),
                  Padding(
                      padding: EdgeInsets.all(10.0),
                      child: Column(
                        crossAxisAlignment: CrossAxisAlignment.start,
                        children: <Widget>[
                          Text(item.title, style: Theme.of(context).textTheme.headline6),
                          Padding(
                            padding: EdgeInsets.only(top: 10.0, bottom: 10.0),
                            child: Text(item.description, style: Theme.of(context).textTheme.caption),
                          ),
                          Flex(
                            direction: Axis.horizontal,
                            children: item.tags.map((e)=>
                                Padding(
                                    padding: EdgeInsets.only(right: 10.0),
                                    child: Chip(label: Text(e))
                                )
                            ).toList(),
                          ),
                          Flex(
                            direction: Axis.horizontal,
                            children: <TextButton>[
                              TextButton(
                                onPressed: onEdit,
                                child: Text('EDIT'),
                              ),
                              TextButton(
                                  onPressed: onDelete,
                                  child: Text('DELETE'),
                                  style: ButtonStyle(foregroundColor: MaterialStateProperty.resolveWith((states) => Colors.red))
                              ),
                            ],
                          )
                        ],
                      )
                  ),
                ],
              )
          )
      ),
    );
  }
}