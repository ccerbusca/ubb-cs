#include <iostream>
#include <vector>
#include "TestP10.h"
#include "p10.h"

void myTest() {
	std::vector<int> vector{100, 500, -1, -20, -100, -500, 40, -2, -3, -4, 1, 2, 3, 4, 5};
	std::cout<<computeSum(vector, 3)<<std::endl;
}

int main() {
	testP10();
	//myTest();
	return 0;
}