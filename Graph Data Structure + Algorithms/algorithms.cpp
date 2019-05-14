//
// Created by Cristian Cerbusca on 2019-04-16.
//

#include "algorithms.h"
#include "Graph.h"
#include <queue>
#include <map>
#include <algorithm>
#include <iostream>
#include <limits.h>

std::vector<int> forwardBFSsearch(Graph g, int v1, int v2) {
	std::vector<int> visited;
	visited.push_back(v1);
	std::vector<int> length, first;
	first.push_back(-1);
	int index = 0;
	while (true) {
		int x = visited[index];
		index++;
		for (const auto & i : g.parseOutbound(x)) {
			if (i == v2) {
				std::vector<int> result;
				first.push_back(index - 1);
				visited.push_back(v2);
				result.push_back(v2);
				int current = first[first.size() - 1];
				while (true) {
					result.push_back(visited[current]);
					current = first[current];
					if (current == -1)
						break;
				}
				std::reverse(result.begin(), result.end());
				return result;
			} else if (std::find(visited.begin(), visited.end(), i) == visited.end()) {
				visited.push_back(i);
				first.push_back(index - 1);
			}
		}
		if (index == visited.size())
			break ;
	}
	return std::vector<int>();
}

std::vector<int> dynProgMinCostWalk(Graph g, int v1, int v2) {
	int maxWalkLen = g.numberOfVertices();
	std::vector<std::vector<int>> w(maxWalkLen + 1, std::vector<int>(g.numberOfVertices(), INT_MAX));

	w[0][v1] = 0;
	int k = 0;
	bool equalLines = true;
	for (k = 1; k < maxWalkLen; k++) {
		for (int x = 0; x < g.numberOfVertices(); x++) {
			int minCost = INT_MAX;
			for (auto y : g.parseInbound(x)) {
				if (w[k - 1][y] == INT_MAX) continue;
				minCost = std::min(minCost, w[k - 1][y] + g.getCost(y, x));
			}
			w[k][x] = std::min(w[k - 1][x], minCost);
			if (w[k - 1][x] != w[k][x])
				equalLines = false;
		}
		if (equalLines)
			break;
		else
			equalLines = true;
	}
	k = maxWalkLen;
	for (int x = 0; x < g.numberOfVertices(); x++) {
		int minCost = INT_MAX;
		for (auto y : g.parseInbound(x)) {
			if (w[k - 1][y] == INT_MAX) continue;
			minCost = std::min(minCost, w[k - 1][y] + g.getCost(y, x));
		}
		w[k][x] = std::min(w[k - 1][x], minCost);
		if (w[k - 1][x] > w[k][x])
			throw std::runtime_error("Negative cost cycle");
	}

	int best = INT_MAX;
	int besti = -1;
	for (int i = 0; i < maxWalkLen; i++) {
		if (w[i][v2] < best) {
			besti = i;
			best = w[i][v2];
		}
	}

	if (best == INT_MAX)
		return std::vector<int>();
	std::vector<int> path;
	path.push_back(v2);
	int node = v2;
	for (int i = besti - 1; i > -1; i--) {
		for (auto y : g.parseInbound(node)) {
			if (w[i + 1][node] == w[i][y] + g.getCost(y, node)) {
				node = y;
				path.push_back(node);
				break;
			}
		}
	}
	std::reverse(path.begin(), path.end());
	return path;
}