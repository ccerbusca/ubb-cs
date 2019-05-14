//
// Created by Cristian Cerbusca on 2019-04-16.
//

#ifndef GRAFURI_LAB1_ALGORITHMS_H
#define GRAFURI_LAB1_ALGORITHMS_H

#include <vector>
#include "Graph.h"

std::vector<int> forwardBFSsearch(Graph g, int v1, int v2);

std::vector<int> dynProgMinCostWalk(Graph g, int v1, int v2);

#endif //GRAFURI_LAB1_ALGORITHMS_H
