package Collection.MyIList;

import Model.Values.Value;

import java.util.ArrayList;
import java.util.List;

public class MyList<T> implements MyIList<T> {

    private List<T> list;

    public MyList(){
        list= new ArrayList<>();
    }

    public int size(){
        return list.size();
    }

    public boolean isEmpty(){
        return list.isEmpty();
    }

    public synchronized void add(T obj){
        list.add(obj);
    }

    public void clear(){
        list.clear();
    }

    public T get(int i){
        return list.get(i);
    }

    @Override
    public List<T> getAll() {
        return list;
    }

    public String toString(){
        return list.toString();
    }
}
