//
// Created by Cristian Cerbusca on 2019-03-19.
//

#ifndef GRAFURI_LAB1_DIRECTEDGRAPH_H
#define GRAFURI_LAB1_DIRECTEDGRAPH_H

#include <string>
#include <vector>
#include <map>

class Graph {
private:
	int                                 vertices;
	std::map<int, std::vector<int>>     out;
	std::map<int, std::vector<int>>     in;
	std::map<std::pair<int, int>, int>  cost;
public:
	const int numberOfVertices() const { return vertices; };
	explicit Graph(std::string fileName);
	explicit Graph(int vertices);
	Graph(Graph& g);
	std::vector<int> parseVertices();
	void    addVertex();
	bool    removeVertex(int n);
	bool    addEdge(int v1, int v2, int Cost);
	bool    isEdge(int v1, int v2);
	bool    removeEdge(int v1, int v2);
	std::vector<int>    parseOutbound(int vertex);
	std::vector<int>    parseInbound(int vertex);
	bool    modifyCost(int v1, int v2, int newCost);
	int     getCost(int v1, int v2);
	bool    isVertex(int vertex);
	int     inDegree(int vertex);
	int     outDegree(int vertex);
	std::string toString();
};

#endif //GRAFURI_LAB1_DIRECTEDGRAPH_H
