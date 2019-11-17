package model.collections.queue;

import java.util.Collection;
import java.util.Deque;
import java.util.LinkedList;
import java.util.Objects;
import java.util.stream.Collectors;

public class Queue<T> implements IQueue<T> {

    private Deque<T> queue = new LinkedList<>();

    @Override
    public void enqueue(T e) {
        queue.addLast(e);
    }

    @Override
    public T getLast() {
        return queue.pop();
    }

    @Override
    public Collection<T> getAll()
    {
        return queue;
    }

    @Override
    public String toString()
    {
        return queue.stream()
                .map(Objects::toString)
                .collect(Collectors.joining("\n"));
    }
}
