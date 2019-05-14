//
// Created by Cristian Cerbusca on 2019-05-08.
//

#include "Heap.h"

Heap::Heap(int k) {
	arr = new int[k];
	_size = k;
	index = 0;
}

Heap::~Heap() {
	delete arr;
}

int Heap::size() const {
	return index;
}

/// Best Case O(1), Worst Case: O(log(n)), Avg Case: O(log(n))
void Heap::bubble_down(int p) {
	int poz = p;
	int elem = arr[p];
	while (poz < index) {
		int maxChild = -1;
		if (poz * 2 + 1 < index)
			maxChild = poz * 2 + 1;
		if (poz * 2 + 2 < index and arr[poz * 2 + 2] < arr[poz * 2 + 1])
			maxChild = poz * 2 + 2;
		if (maxChild != -1 and arr[maxChild] < elem) {
			std::swap(arr[poz], arr[maxChild]);
			poz = maxChild;
		} else
			poz = index;
	}
}

/// Best Case O(1), Worst Case: O(log(n)), Avg Case: O(log(n))
void Heap::bubble_up(int p) {
	int poz = p;
	int elem = arr[p];
	int parent = poz / 2 - (poz % 2 == 0);
	while (poz > 0 and elem < arr[parent]) {
		arr[poz] = arr[parent];
		poz = parent;
		parent = poz / 2 - (poz % 2 == 0);
	}
	arr[poz] = elem;
}

/// Best Case O(1), Worst Case: O(log(n)), Avg Case: O(log(n))
TElem Heap::remove() {
	if (_size == 0)
		return NULL_TELEM;
	TElem deletedElem = arr[0];
	arr[0] = arr[index - 1];
	index--;
	bubble_down(0);
	return deletedElem;
}

TElem& Heap::operator[](int i) {
	return arr[i];
}

void Heap::add(TElem e) {
	if (index == _size) {
		_size *= 2;
		int *newArr = new int[_size];
		for (int i = 0; i < index; i++) {
			newArr[i] = arr[i];
		}
		delete arr;
		arr = newArr;
	}
	arr[index++] = e;
	bubble_up(index - 1);
}