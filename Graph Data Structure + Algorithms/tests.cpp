//
// Created by Cristian Cerbusca on 2019-04-16.
//

#include "tests.h"
#include "Graph.h"
#include <assert.h>
#include <algorithm>

void test_numberOfVertices() {
	Graph a(2);
	assert(a.numberOfVertices() == 2);
}

void test_parseVertices() {
	Graph a(2);
	int index = 0;
	for (const auto & i : a.parseVertices()) {
		assert(i == index);
		index++;
	}
}

void test_addVertex() {
	Graph a(2);
	a.addVertex();
	assert(a.numberOfVertices() == 3);
}

void test_inDegree() {
	Graph a(3);
	a.addEdge(0, 1, 2);
	assert(a.inDegree(1) == 1);
	a.addEdge(2, 1, 3);
	assert(a.inDegree(1) == 2);
}

void test_outDegree() {
	Graph a(3);
	a.addEdge(0, 1, 2);
	assert(a.outDegree(0) == 1);
	a.addEdge(0, 2, 2);
	assert(a.outDegree(0) == 2);
}

void test_addEdge() {
	Graph a(3);
	a.addEdge(1, 2, 3);
	assert(a.getCost(1, 2) == 3);
	assert(a.inDegree(2) == 1);
	assert(a.outDegree(1) == 1);
}

void test_isEdge() {
	Graph a(3);
	a.addEdge(1, 2, 1);
	assert(a.isEdge(1, 2));
	assert(!a.isEdge(0, 2));
}

void test_getCost() {
	Graph a(3);
	a.addEdge(1, 2, 3);
	assert(a.getCost(1, 2) == 3);
}

void test_modifyCost() {
	Graph a(3);
	a.addEdge(1, 2, 3);
	a.modifyCost(1, 2, 4);
	assert(a.getCost(1, 2) == 4);
}

void test_parseInbound() {
	Graph a(3);
	a.addEdge(1, 2, 3);
	auto e1 = a.parseInbound(2);
	assert(e1.size() == 1);
	assert(e1.at(0) == 1);
	auto e2 = a.parseInbound(1);
	assert(e2.empty());
}

void test_parseOutbound() {
	Graph a(3);
	a.addEdge(1, 2, 3);
	auto e1 = a.parseOutbound(1);
	assert(e1.size() == 1);
	assert(e1.at(0) == 2);
	auto e2 = a.parseOutbound(2);
	assert(e2.empty());
}

void test_removeVertex() {
	Graph a(4);
	a.addEdge(1, 2, 3);
	a.addEdge(1, 3, 3);
	a.addEdge(1, 0, 3);
	a.addEdge(3, 1, 3);
	a.removeVertex(1);
	assert(a.numberOfVertices() == 3);
	auto it = a.parseVertices();
	assert(std::find(it.begin(), it.end(), 3) == it.end());
	assert(a.parseOutbound(1).empty());
	assert(a.parseOutbound(3).empty());
	assert(a.parseInbound(1).empty());
	assert(a.parseInbound(2).empty());
	Graph b(4);
	b.addEdge(1, 2, 3);
	b.addEdge(1, 3, 3);
	b.addEdge(3, 0, 3);
	b.removeVertex(1);
	assert(b.isEdge(1, 0));
}

void test_removeEdge() {
	Graph a(4);
	a.addEdge(1, 2, 3);
	a.removeEdge(1, 2);
	assert(a.parseOutbound(1).empty());
}

#include "algorithms.h"

void test_BFS1() {
	Graph a(4);
	a.addEdge(0, 1, 1);
	a.addEdge(1, 3, 1);
	a.addEdge(2, 1, 1);
	a.addEdge(3, 4, 1);
	a.addEdge(4, 3, 1);
	a.addEdge(4, 2, 1);
	auto it = forwardBFSsearch(a, 1, 2);
	assert(it.at(0) == 1);
	assert(it.at(1) == 3);
	assert(it.at(2) == 4);
	assert(it.at(3) == 2);
	assert(it.size() == 4);
}

void test_BFS2() {
	Graph a(4);
	a.addEdge(0, 1, 1);
	a.addEdge(0, 2, 1);
	a.addEdge(1, 2, 1);
	a.addEdge(2, 3, 1);
	a.addEdge(2, 4, 1);
	auto it = forwardBFSsearch(a, 0, 3);
	assert(it.at(0) == 0);
	assert(it.at(1) == 2);
	assert(it.at(2) == 3);
}

#include <iostream>

void test_dynProgMinCostWalk1() {
	Graph a(9);
	a.addEdge(1, 5, 10);
	a.addEdge(2, 1, 11);
	a.addEdge(5, 3, 1);
	a.addEdge(2, 3, 2);
	a.addEdge(3, 7, 2);
	a.addEdge(7, 3, 13);
	a.addEdge(3, 8, 8);
	a.addEdge(5, 4, 5);
	a.addEdge(4, 8, 50);
	a.addEdge(4, 6, 7);
	a.addEdge(5, 6, 6);
	auto it = dynProgMinCostWalk(a, 1, 8);
	assert(it == forwardBFSsearch(a, 1, 8));
}

void test_dynProgMinCostWalk2() {
	Graph a(7);
	a.addEdge(1, 2, 1);
	a.addEdge(1, 5, 1);
	a.addEdge(5, 6, 1);
	a.addEdge(2, 3, 1);
	a.addEdge(3, 4, 1);
	a.addEdge(5, 6, 1);
	auto it = dynProgMinCostWalk(a, 1, 6);
	assert(it == forwardBFSsearch(a, 1, 6));
}

void test_dynProgMinCostWalk3() {
	Graph a(3);
	a.addEdge(0, 1, 2);
	a.addEdge(2, 0, 1);
	a.addEdge(2, 1, 4);
	auto it = dynProgMinCostWalk(a, 2, 1);
	assert(it.at(0) == 2);
	assert(it.at(1) == 0);
	assert(it.at(2) == 1);
}


void test_dynProgMinCostWalk_negativeCost() {
	Graph a(4);
	a.addEdge(0, 1, 1);
	a.addEdge(1, 2, -1);
	a.addEdge(2, 3, -1);
	a.addEdge(3, 0, -1);
	try {
		auto it = dynProgMinCostWalk(a, 0, 3);
		assert(false);
	} catch (std::runtime_error& error) {
		assert(true);
	}
}

void testAll() {
	test_numberOfVertices();
	test_parseVertices();
	test_inDegree();
	test_outDegree();
	test_getCost();
	test_addEdge();
	test_isEdge();
	test_addVertex();
	test_modifyCost();
	test_parseInbound();
	test_parseOutbound();
	test_removeVertex();
	test_removeEdge();
	test_BFS1();
	test_BFS2();
	test_dynProgMinCostWalk1();
	test_dynProgMinCostWalk2();
	test_dynProgMinCostWalk_negativeCost();
	test_dynProgMinCostWalk3();
}