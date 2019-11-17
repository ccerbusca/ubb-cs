package model.collections.stack;

public interface IStack<T> {
    T pop();
    void push(T v);
    boolean isEmpty();
}
