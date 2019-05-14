//
// Created by Cristian Cerbusca on 2019-04-30.
//

#include <stdexcept>
#include <iostream>
#include "p10.h"
#include "Heap.h"

/// Best Case O(k), Worst Case: O(n * log(k)), Avg Case: O(n * log(k))
long computeSum(std::vector<TElem> vector, int k) {
	if (k <= 0)
		throw std::runtime_error("K cannot be less than or equal to zero");
	if (k > vector.size())
		k = vector.size();
	Heap heap(k);
	for (int i = 0; i < k; i++) {
		heap.add(vector[i]);
	}
	for (int i = k; i < vector.size(); i++){
		if (vector[i] > heap[0]) {
			heap[0] = vector[i];
			heap.bubble_down(0);
		}
	}
	int s = 0;
	for (int i = 0; i < k; i++) {
		s += heap[i];
	}
	return s;
}