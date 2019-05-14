//
// Created by Cristian Cerbusca on 2019-05-08.
//

#ifndef SDA_LAB5_HEAP_H
#define SDA_LAB5_HEAP_H


#include "p10.h"

class Heap {
private:
	int *arr;
	int _size;
	int index;
public:
	Heap(int k);
	~Heap();
	void add(TElem e);
	void bubble_down(int p);
	void bubble_up(int p);
	TElem remove();
	TElem& operator[](int index);
	int size() const;
};


#endif //SDA_LAB5_HEAP_H
