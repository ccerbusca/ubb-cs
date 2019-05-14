#pragma once
#include<vector>
#include<utility>
#include "MultiMapIterator.h"

class MultiMapIterator;

typedef int TKey;

typedef int TValue;

typedef std::pair<TKey, TValue> TElem;

struct DLLNode {
	TElem       elem;
	DLLNode     *next;
	DLLNode     *prev;
};

struct DLL {
	DLLNode     *head;
	DLLNode     *tail;
};



class MultiMap
{
	friend class MultiMapIterator;
private:
	DLL     list;
	int     _size;

public:
	//constructor
	MultiMap();


	//adds a key value pair to the multimap
	void add(TKey c, TValue v);

	//removes a key value pair from the multimap
	//returns true if the pair was removed (if it was in the multimap) and false otherwise
	bool remove(TKey c, TValue v);

	//returns the vector of values associated to a key. If the key is not in the MultiMap, the vector is empty
	std::vector<TValue> search(TKey c) const;

	//returns the number of pairs from the multimap
	int size() const;

	//checks whether the multimap is empty
	bool isEmpty() const;

	//returns an iterator for the multimap
	MultiMapIterator iterator() const;

	//returns a vector with all the keys from the MultiMap
	std::vector<TKey> keySet() const;

	//destructor
	~MultiMap();
};



