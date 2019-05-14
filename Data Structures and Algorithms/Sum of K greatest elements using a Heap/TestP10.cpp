#include "TestP10.h"
#include <vector>
#include "p10.h"
#include <assert.h>
#include <numeric>
#include <cstdlib>
#include <iostream>

using namespace std;

vector<int> randomFromInterval(int min, int max, int k) {
	vector<int> values;
	for (int v = min; v <= max; v++) {
		values.push_back(v);
	}
	int n = values.size();
	for (int i = 0; i < n - 1; i++) {
		int j = i + rand() % (n - i);
		swap(values[i], values[j]);
	}
	for (int i = values.size() - 1; i >= k; i--) {
		values.pop_back();
	}
	return values;
}


void testException() {
	vector<int> v = { 1, 2, 3, 4, 5 };
	vector<int> kNegative = randomFromInterval(-50, -1, 10);
	for (int i = 0; i < (int)kNegative.size(); i++) {
		try {
			computeSum(v, kNegative[i]);
			assert(false);
		}
		catch (exception& ex) {
			assert(true);
		}
	}
}

void testSum(int k) {
	vector<int> v;

	int min1 = -1000;
	int max1 = 1000;

	int min2 = max1 + 1;
	int max2 = min2 + k - 1;

	vector<int> valuesI1 = randomFromInterval(min1, max1, max1 - min1 + 1);
	for (int i = 0; i < (int)valuesI1.size() / 2; i++) {
		v.push_back(valuesI1[i]);
	}

	vector<int> valuesI2 = randomFromInterval(min2, max2, k);
	for (int i = 0; i < k; i++) {
		v.push_back(valuesI2[i]);
	}

	for (int i = valuesI1.size() / 2; i < (int)valuesI1.size(); i++) {
		v.push_back(valuesI1[i]);
	}

	long sum = std::accumulate(valuesI2.begin(), valuesI2.end(), 0);
	try {
		assert(computeSum(v, k) == sum);
	}
	catch (exception& e) {
		assert(false);
	}
}

void testSumAll() {
	int min = -1000;
	int max = 1000;
	int kMin = 100;
	vector<int> v = randomFromInterval(min, max, kMin);
	long sum = std::accumulate(v.begin(), v.end(), 0);
	for (int k = kMin; k <= kMin + 100; k++) {
		try {
			assert(computeSum(v, k) == sum);
		}
		catch (exception& e) {
			assert(false);
		}
	}

}



void testP10() {
	testException();
	testSum(10);
	testSum(20);
	testSum(100);
	testSum(1000);
	testSumAll();
}
