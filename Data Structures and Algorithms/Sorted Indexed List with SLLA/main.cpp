#include <iostream>
#include <assert.h>
#include "ShortTest.h"
#include "ExtendedTest.h"
#include "SortedIndexedList.h"

void test_removeFromKtoK() {
	SortedIndexedList l = SortedIndexedList([](TComp a, TComp b) {return a <= b; });
	l.add(1);
	l.add(2);
	l.add(3);
	l.add(4);
	l.add(5);
	l.add(6);
	int ret = l.removeFromKtoK(2);
	assert(ret == 3);
	assert(l.size() == 3);
	assert(l.search(2) == -1);
	assert(l.search(4) == -1);
	assert(l.search(6) == -1);
	auto it = l.iterator();
	assert(it.getCurrent() == 1);
	it.next();
	assert(it.getCurrent() == 3);
	it.next();
	assert(it.getCurrent() == 5);
	it.next();
	assert(!it.valid());
}

int main() {
	testAll();
	testAllExtended();
	test_removeFromKtoK();
	return 0;
}