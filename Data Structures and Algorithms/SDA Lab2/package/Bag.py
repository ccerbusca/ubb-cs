"""
Created on Tue Feb 19 15:48:58 2019

@author: Zsu
"""


class Bag:

    # creates a new, empty Bag
    def __init__(self):
        self.__elems = []
        self.__freq = []

    # adds a new element to the Bag
    def add(self, e):
        # O(n) worst case, O(1) best case
        if e in self.__elems:
            self.__freq[self.__elems.index(e)] += 1
        else:
            self.__elems.append(e)
            self.__freq.append(1)

    # removes one occurrence of an element from a Bag
    # returns True if an element was actually removed (the Bag contained the element e), or False if nothing was removed
    def remove(self, e):
        # O(1)
        if e in self.__elems:
            index = self.__elems.index(e)
            if self.__freq[index] == 1:
                del self.__freq[index]
                del self.__elems[index]
            else:
                self.__freq[self.__elems.index(e)] -= 1
            return True
        return False

    # searches for an element e in the Bag
    # returns True if the Bag contains the element, False otherwise
    def search(self, e):
        # O(n) worst case, O(1) best case
        return e in self.__elems

    # counts and returns the number of times the element e appears in the bag
    def nrOccurrences(self, e):
        # 0(n) worst case, O(1) best case
        if self.search(e):
            return self.__freq[self.__elems.index(e)]
        return 0

    # returns the size of the Bag (the number of elements)
    def size(self):
        # O(n)
        return sum(self.__freq)

    # returns True if the Bag is empty, False otherwise
    def isEmpty(self):
        # 0(1)
        return self.size() == 0

    # returns a BagIterator for the Bag
    def iterator(self):
        # 0(1)
        return BagIterator(self)


class BagIterator:

    # creates an iterator for the Bag b, set to the first element of the bag, or invalid if the Bag is empty
    def __init__(self, b):
        self.__bag = b
        self.__index = 0
        self.__findex = 0

    # returns True if the iterator is valid
    def valid(self):
        # 0(1)
        return self.__index < len(self.__bag._Bag__elems)

    # returns the current element from the iterator.
    # throws ValueError if the iterator is not valid
    def getCurrent(self):
        # 0(1)
        if not self.valid():
            raise ValueError("Iterator not valid")
        return self.__bag._Bag__elems[self.__index]

    # moves the iterator to the next element
    # throws ValueError if the iterator is not valid
    def next(self):
        # 0(1)
        if not self.valid():
            raise ValueError("Iterator not valid")
        if self.__findex + 1 < self.__bag._Bag__freq[self.__index]:
            self.__findex += 1
        else:
            self.__index += 1
            self.__findex = 0

    # sets the iterator to the first element from the Bag
    def first(self):
        # 0(1)
        self.__index = 0
        self.__findex = 0
