//
// Created by Cristian Cerbusca on 2019-04-16.
//

#ifndef GRAFURI_LAB1_RANDOMGRAPH_H
#define GRAFURI_LAB1_RANDOMGRAPH_H


#include <numeric>
#include "Graph.h"
#include <random>

class RandomGraph {
private:
	template<typename Iter, typename RandomGenerator>
	static Iter select_randomly(Iter start, Iter end, RandomGenerator& g) {
		std::uniform_int_distribution<> dis(0, std::distance(start, end) - 1);
		std::advance(start, dis(g));
		return start;
	}

	template<typename Iter>
	static Iter select_randomly(Iter start, Iter end) {
		static std::random_device rd;
		static std::mt19937 gen(rd());
		return select_randomly(start, end, gen);
	}
public:
	/**
	 *
	 * @param vertices
	 * @param edges
	 * @return
	 */
	static Graph generate(int vertices, int edges) {
		Graph graph(vertices);
		std::vector<int> set_vertices(vertices);
		std::iota(set_vertices.begin(), set_vertices.end(), 0);
		std::random_device dev;
		std::mt19937 rng(dev());
		std::uniform_int_distribution<std::mt19937::result_type> dist(1, 300);
		int index = 0;
		while (index <= edges) {
			int start = *select_randomly(set_vertices.begin(), set_vertices.end());
			int end = *select_randomly(set_vertices.begin(), set_vertices.end());
			int cost = dist(rng);
			if (graph.addEdge(start, end, cost))
				index++;
		}
		return graph;
	}
};


#endif //GRAFURI_LAB1_RANDOMGRAPH_H
