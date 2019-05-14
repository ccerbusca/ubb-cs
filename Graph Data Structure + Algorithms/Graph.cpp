//
// Created by Cristian Cerbusca on 2019-03-19.
//

#include "Graph.h"
#include <fstream>
#include <algorithm>

Graph::Graph(int vertices): vertices{vertices} {
	for (int i = 0; i < vertices; i++) {
		out[i] = std::vector<int>();
		in[i] = std::vector<int>();
	}
}

Graph::Graph(Graph &g) {
	vertices = g.vertices;
	out = g.out;
	in = g.in;
	cost = g.cost;
}

Graph::Graph(std::string fileName) {
	std::ifstream fin(fileName);
	int vertices1, edges;
	fin>>vertices1>>edges;
	vertices = vertices1;
	for (int i = 0; i < edges; i++) {
		int v1, v2, cost1;
		fin>>v1>>v2>>cost1;
		addEdge(v1, v2, cost1);
	}
	fin.close();
}

std::vector<int> Graph::parseVertices() {
	std::vector<int> keys;
	for (const auto& element : in) {
		keys.push_back(element.first);
	}
	return keys;
}

void Graph::addVertex() {
	in[vertices] = std::vector<int>();
	out[vertices] = std::vector<int>();
	vertices++;
}

int Graph::getCost(int v1, int v2) {
	if (this->isEdge(v1, v2))
		return cost[{v1, v2}];
	if (v1 == v2)
		return 0;
	return -1;
}

bool Graph::modifyCost(int v1, int v2, int newCost) {
	if (isEdge(v1, v2)) {
		cost[{v1, v2}] = newCost;
		return true;
	}
	return false;
}

bool Graph::isEdge(int v1, int v2) {
	if (out.find(v1) != out.end())
		if (std::find(out[v1].begin(), out[v1].end(), v2) != out[v1].end())
			return true;
	return false;
}

bool Graph::addEdge(int v1, int v2, int Cost) {
	if (!isEdge(v1, v2)){
		in[v2].push_back(v1);
		out[v1].push_back(v2);
		cost[{v1, v2}] = Cost;
		return true;
	}
	return false;
}

bool Graph::isVertex(int vertex) {
	auto elements = parseVertices();
	return std::find(elements.begin(), elements.end(), vertex) != elements.end();
}

std::vector<int> Graph::parseInbound(int vertex) {
	if (isVertex(vertex))
		return in[vertex];
	return std::vector<int>();
}
std::vector<int> Graph::parseOutbound(int vertex) {
	if (isVertex(vertex))
		return out[vertex];
	return std::vector<int>();
}

bool Graph::removeVertex(int vertex) {
	if (!isVertex(vertex))
		return false;
	if (vertex == vertices - 1) {
		in.erase(vertex);
		out.erase(vertex);
		auto it = cost.cbegin();
		while (it != cost.cend()) {
			if (it->first.first == vertex || it->first.second == vertex)
				it = cost.erase(it);
			else
				it++;
		}
		for (auto & i : in) {
			i.second.erase(
					std::remove(i.second.begin(), i.second.end(), vertex),
					i.second.end());
		}
		for (auto & i : out) {
			i.second.erase(
					std::remove(i.second.begin(), i.second.end(), vertex),
					i.second.end());
		}
	} else {
		auto lastIn = in[vertices - 1];
		auto lastOut = out[vertices - 1];
		in.erase(vertices - 1);
		out.erase(vertices - 1);
		in.erase(vertex);
		out.erase(vertex);
		in[vertex] = lastIn;
		out[vertex] = lastOut;
		for (auto& i : in) {
			i.second.erase(
					std::remove(i.second.begin(), i.second.end(), vertex),
					i.second.end());
			auto removed = std::remove(i.second.begin(), i.second.end(), vertices - 1);
			if (removed != i.second.end()) {
				i.second.erase(removed, i.second.end());
				i.second.push_back(vertex);
			}
		}
		for (auto& i : out) {
			i.second.erase(
					std::remove(i.second.begin(), i.second.end(), vertex),
					i.second.end());
			auto removed = std::remove(i.second.begin(), i.second.end(), vertices - 1);
			if (removed != i.second.end()) {
				i.second.erase(removed, i.second.end());
				i.second.push_back(vertex);
			}
		}
		for (int i = 0; i < vertices - 1; i++) {
			if (cost.find({i, vertex}) != cost.end())
				cost.erase({i, vertex});
			if (cost.find({vertex, i}) != cost.end())
				cost.erase({vertex, i});
			if (cost.find({i, vertices - 1}) != cost.end()) {
				int aux = cost[{i, vertices - 1}];
				cost.erase({i, vertices - 1});
				cost[{i, vertex}] = aux;
			}
			if (cost.find({vertices - 1, i}) != cost.end()) {
				int aux = cost[{vertices - 1, i}];
				cost.erase({vertices - 1, i});
				cost[{vertex, i}] = aux;
			}
		}
	}
	vertices -= 1;
	return true;
}

bool Graph::removeEdge(int v1, int v2) {
	if (!isEdge(v1, v2))
		return false;
	for (auto & i : in) {
		i.second.erase(
				std::remove(i.second.begin(), i.second.end(), v2),
				i.second.end());
	}
	for (auto & i : out) {
		i.second.erase(
				std::remove(i.second.begin(), i.second.end(), v2),
				i.second.end());
	}
	if (cost.find({v1, v2}) != cost.end())
		cost.erase({v1, v2});
	return true;
}

int Graph::inDegree(int vertex) {
	return in[vertex].size();
}

int Graph::outDegree(int vertex) {
	return out[vertex].size();
}

std::string Graph::toString() {
	std::string s;
	s += "Outbound:\n";
	for (const auto & i : out) {
		if (i.second.size() > 0) {
			s += "\t" + std::to_string(i.first) + " -> (";
			int index = 0;
			for (const auto &j : i.second) {
				s += std::to_string(j) + (index++ < i.second.size() - 1 ? ", " : ")");
			}
			s += "\n";
		}
	}
	s += "Inbound:\n";
	for (const auto & i : in) {
		if (i.second.size() > 0) {
			s += "\t" + std::to_string(i.first) + " -> (";
			int index = 0;
			for (const auto &j : i.second) {
				s += std::to_string(j) + (index++ < i.second.size() - 1 ? ", " : ")");
			}
			s += "\n";
		}
	}
	s += "Costs:\n";
	for (const auto & i : cost) {
		s += "\t(" + std::to_string(i.first.first)+ ", " + std::to_string(i.first.second) + ") -> " + std::to_string(i.second) + "\n";
	}
	return s;
}





