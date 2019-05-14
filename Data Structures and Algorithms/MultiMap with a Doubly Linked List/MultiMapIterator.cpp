//
// Created by Cristian Cerbusca on 2019-04-02.
//

#include <stdexcept>
#include "MultiMapIterator.h"

MultiMapIterator::MultiMapIterator(const MultiMap &c): c{c}, current{c.list.head} { }

/// theta(1)
void MultiMapIterator::first() {
	current = c.list.head;
}

/// theta(1)
void MultiMapIterator::next() {
	if (valid())
		current = current->next;
}

/// theta(1)
bool MultiMapIterator::valid() const {
	return current != nullptr;
}

/// theta(1)
TElem MultiMapIterator::getCurrent() const {
	if (valid())
		return current->elem;
	else
		throw std::runtime_error("Iterator is not valid");
}