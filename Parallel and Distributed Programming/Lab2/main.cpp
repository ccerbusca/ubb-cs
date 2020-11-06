#include <iostream>
#include <condition_variable>
#include "ThreadSafeQueue.hpp"
#include <limits>

void scalarProduct(std::vector<int>& a, std::vector<int>& b) {
    if (a.size() != b.size())
        throw std::exception("Vectors of different sizes");
    ThreadSafeQueue<int> threadSafeQueue = ThreadSafeQueue<int>(5);
    std::thread th([&]() {
        for (int i = 0; i < a.size(); i++) {
            int pairProd = a[i] * b[i];
            threadSafeQueue.enqueue(pairProd);
        }
        threadSafeQueue.enqueue(std::numeric_limits<int>::max());
    });
    std::thread th_sum([&]() {
        int sum = 0;
        while (true) {
            int k = threadSafeQueue.pop();
            if (k == std::numeric_limits<int>::max()) {
                break;
            }
            sum += k;
        }
        std::cout << sum << std::endl;
        std::cout.flush();
    });
    th.join();
    th_sum.join();
}

int main() {
    int arr1[] = {1, 2, 3, 4, 5};
    int arr2[] = {1, 2, 3, 4, 5};

    std::vector<int> a (arr1, arr1 + sizeof(arr1) / sizeof(int));
    std::vector<int> b (arr2, arr2 + sizeof(arr2) / sizeof(int));

    scalarProduct(a, b);
    return 0;
}
