//
// Created by crist on 2020-10-26.
//

#include <condition_variable>
#include <condition_variable>

#ifndef LAB2_THREADSAFEQUEUE_H
#define LAB2_THREADSAFEQUEUE_H

template <typename T>
class ThreadSafeQueue {
public:
    explicit ThreadSafeQueue(int n): size{n}, count{0} {
        arr = new T[n];
    }

    void enqueue(T a) {
        std::unique_lock<std::recursive_mutex> lk(mtx);
        while (full()) {
            queue_not_full.wait(lk);
        }
        arr[count++] = a;
        queue_not_empty.notify_one();
    }

    T pop() {
        std::unique_lock<std::recursive_mutex> lk(mtx);
        while(empty()) {
            queue_not_empty.wait(lk);
        }
        T result = arr[--count];
        queue_not_full.notify_one();
        return result;
    }

    bool full() {
        std::lock_guard<std::recursive_mutex> lk(mtx);
        return count == size;
    }

    bool empty() {
        std::lock_guard<std::recursive_mutex> lk(mtx);
        return count == 0;
    }

private:
    T* arr;
    int count, size;

    std::recursive_mutex mtx;
    std::condition_variable_any queue_not_empty;
    std::condition_variable_any queue_not_full;
};

#endif //LAB2_THREADSAFEQUEUE_H
