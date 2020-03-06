package Collection.MyIList;

import Model.Values.Value;

import java.util.List;

public interface MyIList<T> {
    int size();
    boolean isEmpty();
    void add(T obj);
    void clear();
    T get(int index);
    List<T> getAll();
    String toString();
}
