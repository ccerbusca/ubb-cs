package model.collections.stack;

import java.util.Deque;
import java.util.LinkedList;
import java.util.Objects;
import java.util.stream.Collectors;

public class Stack<T> implements IStack<T> {

    private Deque<T> stack = new LinkedList<>();

    @Override
    public T pop() {
        return stack.pop();
    }

    @Override
    public void push(T v) {
        stack.push(v);
    }

    @Override
    public boolean isEmpty()
    {
        return stack.isEmpty();
    }

    @Override
    public String toString()
    {
        return stack.stream()
                .map(Objects::toString)
                .collect(Collectors.joining("\n"));
    }
}
