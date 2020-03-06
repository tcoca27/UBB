package Collection.Stack;

import java.util.Stack;

public interface MyIStack<T> {
    T pop();
    void push(T obj);
    boolean isEmpty();
    Stack<T> getAll();
    String toString();
}
