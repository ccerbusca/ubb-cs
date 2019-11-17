package model.collections.queue;

import java.util.Collection;

public interface IQueue<T> {
    void enqueue(T e);
    T getLast();
    Collection<T> getAll();
}
