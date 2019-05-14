//
// Created by Cristian Cerbusca on 2019-04-30.
//

#ifndef SDA_LAB5_P10_H
#define SDA_LAB5_P10_H

#include <vector>

typedef int TElem;
#define NULL_TELEM -1000000000

//computes the sum of the largest k elements from the vector
//if k is less than or equal to 0, it throws an exception
long computeSum(std::vector<TElem> vector, int k);


#endif //SDA_LAB5_P10_H
