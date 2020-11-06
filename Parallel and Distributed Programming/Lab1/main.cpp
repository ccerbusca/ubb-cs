#include <iostream>
#include <utility>
#include <vector>
#include <numeric>
#include <algorithm>
#include <chrono>
#include <thread>
#include <mutex>
#include <ctime>
#include <random>
#include <cstdlib>
#include "string"
#include <memory>
#include <fstream>
#include <shared_mutex>

class Variable {
public:
    virtual int compute() = 0;

    void registerDependent(Variable* variable) {
        dependents.push_back(variable);
    }

    void registerDependency(Variable* variable) {
        dependencies.push_back(variable);
    }

    virtual void check() {}
    virtual void recompute(int difference) {}
    virtual void log() = 0;

    void notifyChanged(int difference) {
        for (Variable* variable: dependents) {
            variable->recompute(difference);
        }
    }

protected:
    std::mutex mtx;
    std::vector<Variable*> dependents;
    std::vector<Variable*> dependencies;
};

class Primary : public Variable {
private:
    int value;
public:
    Primary(int value) : value{value} {}

    Primary() : value{0} {}

    int compute() override {
        return value;
    }

    void setNewValue(int newValue) {
        value = newValue;
        notifyChanged(value - newValue);
    }

    void verify() {
        for (Variable* variable : dependents) {
            variable->check();
        }
    }

    void log() override {
        std::cout<<"Primary{" + std::to_string(value) + "}"<<std::endl;
        for (Variable* variable : dependents) {
            variable->log();
            std::cout << std::endl;
        }
    }
};

class Secondary : public Variable {
private:
    int value;

    int dep_sum() {
        int sum = 0;
        for (Variable* variable : dependencies) {
            sum += variable->compute();
        }
        return sum;
    }
public:
    Secondary() {}

    int compute() override {
        value = dep_sum();
        return value;
    }

    void check() override {
        auto depsum = dep_sum();
        if (depsum != value) {
            mtx.lock();

            std::cout<< value << " " << depsum << std::endl;
            mtx.unlock();
        }
    }

    void recompute(int difference) override {
        if (difference != 0) {
            mtx.lock();
            value += difference;
            mtx.unlock();
            notifyChanged(difference);
        }
    }

   void log() override {
        std::cout<< "Secondary {" + std::to_string(value) + ", [";
        std::cout.flush();
        for (Variable* variable : dependents) {
            variable->log();
        }
        std::cout<< "] }";
    }
};

std::vector<Primary*> read_deps()
{
    std::ifstream in("D:\\Sem 5\\PDP\\Lab1\\file.txt");
    int nprimary;
    in >> nprimary;
    std::vector<Primary*> vprimary;
    for (int i = 0; i < nprimary; i++) {
        vprimary.push_back(new Primary{});
    }

    int nsecond;
    in >> nsecond;
    std::vector<Secondary*> vsecond;
    for (int i = 0; i < nsecond; i++) {
        vsecond.push_back(new Secondary{});
    }

    vsecond.reserve(nsecond);
    for (int i = 0; i < nsecond; i++) {
        int ndeps;
        in >> ndeps;
        int type, nr;
        for (int j = 0; j < ndeps; j++) {
            in >> type >> nr;
            if (type == 1) {
                vsecond[i]->registerDependency(vprimary[nr - 1]);
                vprimary[nr - 1]->registerDependent(vsecond[i]);
            } else if (type == 2) {
                vsecond[i]->registerDependency(vsecond[nr - 1]);
                vsecond[nr - 1]->registerDependent(vsecond[i]);
            }
        }
    }

    for (int i = 0; i < nprimary; i++) {
        int n;
        in >> n;
        vprimary[i]->setNewValue(n);
    }

    return vprimary;
}
class Counter {
public:
    void decrement() {
        std::unique_lock lock(mutex);
        MAX_OPERATIONS--;
    }

    int getAndDecrement() {
        std::unique_lock lock(mutex);
        --MAX_OPERATIONS;
        return MAX_OPERATIONS + 1;
    }

    int get() {
        std::shared_lock lock(mutex);
        return MAX_OPERATIONS;
    }

private:
    int MAX_OPERATIONS = 300000;
    mutable std::shared_mutex mutex;
};



int main() {
    int THREADS = 8;
    std::vector<std::thread> threads;
    threads.reserve(THREADS);
    Counter counter = Counter();

    srand(time(nullptr));
    auto primaries = read_deps();

//    for (Primary* primary : primaries) {
//        primary->log();
//    }

    auto start = std::chrono::system_clock::now();
    for (int i = 0; i < THREADS; i++) {
        threads.emplace_back([&] {
            while(counter.getAndDecrement() > 0) {
                int n = rand() % primaries.size();
                primaries[n]->setNewValue(rand() % 1000);
            }
        });
    }

    std::thread verifier([&] {
        while (counter.get() > 0) {
            if (rand() % 100 + 1 < 40) {
                for (Primary* primary : primaries) {
                    primary->verify();
                }
            }
        }
    });

    for (std::thread& thread : threads) {
        thread.join();
    }
    verifier.join();

    auto end = std::chrono::system_clock::now();

    std::chrono::duration<double> elapsed_seconds = end - start;
    std::time_t end_time = std::chrono::system_clock::to_time_t(end);

    std::cout << "\n\n\nfinished computation at " << std::ctime(&end_time)
              << "elapsed time: " << elapsed_seconds.count() << "s\n";

    return 0;
}
