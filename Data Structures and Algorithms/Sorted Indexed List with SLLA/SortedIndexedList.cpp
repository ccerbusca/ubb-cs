//
// Created by Cristian Cerbusca on 2019-04-05.
//

#include <stdexcept>
#include <iostream>
#include "SortedIndexedList.h"

/// Complexity: Worst Case: O(N), Best Case: O(n); Overall: Theta(n)
SortedIndexedList::SortedIndexedList(Relation r): r{r}, _size{0}, list{} {
	list.cap = INIT_CAPACITY;
	list.elems = new TComp[list.cap];
	list.next = new int[list.cap];
	list.head = -1;
	for (int i = 0; i < list.cap; i++) {
		list.next[i] = -1;
	}
	list.next[list.cap - 1] = -1;
	list.firstEmpty = - 1;
}

/// Complexity: Worst Case: O(N), Best Case: O(1); Overall: O(n)
int SortedIndexedList::search(TComp e) const {
	int current = list.head;
	int i = 0;
	while (current != -1 and list.elems[current] != e) {
		i++;
		current = list.next[current];
	}
	if (current == -1)
		return -1;
	return i;
}

/// Complexity: Worst Case: O(N), Best Case: O(n); Overall: Theta(n)
void SortedIndexedList::add(TComp e) {
	if (_size == list.cap)
		list.resize();
	list.elems[_size++] = e;
	int current = list.head;
	int prev = -1;
	if (list.head != -1) {
		while (current != -1 and
				r(list.elems[current], e)) {
			prev = current;
			current = list.next[current];
		}
		if (prev == -1) {
			list.next[_size - 1] = list.head;
			list.head = _size - 1;
		} else {
			list.next[_size - 1] = current;
			list.next[prev] = _size - 1;
		}
	}
	else {
		list.head = _size - 1;
	}

}

/// Complexity: Worst Case: O(N), Best Case: O(n); Overall: Theta(n)
TComp SortedIndexedList::remove(int pos) {
	if (isEmpty())
		throw std::runtime_error("List is empty");
	if (pos >= _size or pos < 0)
		throw std::runtime_error("Position is not valid");
	int current = list.head, prev = -1, i = 0, save;
	while (current != -1 and i < pos) {
		i++;
		prev = current;
		current = list.next[current];
	}
	if (prev == -1) {
		list.head = list.next[current];
		save = list.elems[current];
	} else {
		save = list.elems[current];
		list.next[prev] = list.next[current];
	}
	for (int i = current; i < _size - 1; i++) {
		list.elems[i] = list.elems[i + 1];
		list.next[i] = list.next[i + 1];
	}
	for (int i = 0; i < _size - 1; i++)
		if (list.next[i] > current)
			list.next[i] -= 1;
	_size--;
	if (list.head > current)
		list.head--;
	return save;
}

/// Theta(1)
int SortedIndexedList::size() const { return _size; }

/// Theta(1)
bool SortedIndexedList::isEmpty() const { return _size == 0; }

/// Complexity: Worst Case: O(N), Best Case: O(1); Overall: O(n)
TComp SortedIndexedList::getElement(int pos) const {
	if (isEmpty())
		throw std::runtime_error("List is empty");
	if (pos >= size())
		throw std::runtime_error("Index out of range");
	int current = list.head;
	for (int i = 0; i < pos; i++)
		current = list.next[current];
	return list.elems[current];
}

ListIterator SortedIndexedList::iterator() {
	return ListIterator(*this);
}

SortedIndexedList::~SortedIndexedList() {
	delete[] list.elems;
	delete[] list.next;
}

/// Complexity: Worst Case: O(kn), Best Case: O(1); Overall: O(kn)
int SortedIndexedList::removeFromKtoK(int k) {
	if (k <= 0)
		throw std::invalid_argument("K is less than or equal to 0");
	if (k > size())
		return 0;
	int count = 0;
	int pos = size();
	while (pos > 0) {
		if (pos % k == 0) {
			remove(pos - 1);
			count++;
		}
		pos--;
	}
	return count;
}