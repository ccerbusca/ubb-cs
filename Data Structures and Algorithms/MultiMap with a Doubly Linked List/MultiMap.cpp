//
// Created by Cristian Cerbusca on 2019-04-02.
//

#include <algorithm>
#include "MultiMap.h"

MultiMap::MultiMap(): list(DLL{nullptr, nullptr}), _size(0) { }

///complexity is always theta(1)
int MultiMap::size() const {
	return _size;
}

///operation complexity is theta(1) in all cases
void MultiMap::add(TKey c, TValue v) {
	TElem elem{c, v};
	if (list.tail) {
		list.tail->next = new DLLNode{elem, nullptr, list.tail};
		list.tail = list.tail->next;
	} else {
		list.head = new DLLNode{elem, nullptr, nullptr};
		list.tail = list.head;
	}
	_size++;
}


///operation complexity is theta(n), O(1) in the best case when we remove the first
///element and the worst case is O(n) when we remove the last one
bool MultiMap::remove(TKey c, TValue v) {
	DLLNode *head = list.head;
	if (head == nullptr)
		return false;
	while (head) {
		if (head->elem.first == c and head->elem.second == v) {
			DLLNode *prev = head->prev;
			DLLNode *next = head->next;
			delete head;
			if (prev)
				prev->next = next;
			else
				list.head = next;
			if (next)
				next->prev = prev;
			else
				list.tail = prev;
			_size--;
			return true;
		}
		head = head->next;
	}
	return false;
}

/// operation complexity is theta(1)
bool MultiMap::isEmpty() const { return _size == 0; }

MultiMap::~MultiMap() {
	DLLNode *nextRef;
	DLLNode *head = list.head;
	while (head){
		nextRef = head->next;
		delete head;
		head = nextRef;
		if (nextRef != nullptr)
			nextRef = nextRef->next;
	}
}

///operation complexity is theta(n) in all cases
std::vector<TValue> MultiMap::search(TKey c) const {
	std::vector<TValue> occurences;
	DLLNode *head = list.head;
	if (head == nullptr)
		return occurences;
	while (head) {
		if (head->elem.first == c)
			occurences.push_back(head->elem.second);
		head = head->next;
	}
	return occurences;
}

/// Theta(1)
MultiMapIterator MultiMap::iterator() const {
	return MultiMapIterator{*this};
}

///Theta(n), best case O(n), worst case O(n)
std::vector<TKey> MultiMap::keySet() const {
	std::vector<TKey> keys;
	DLLNode *head = list.head;
	while (head) {
		if (std::find(keys.begin(), keys.end(), head->elem.first) == keys.end())
			keys.push_back(head->elem.first);
		head = head->next;
	}
	return keys;
}

