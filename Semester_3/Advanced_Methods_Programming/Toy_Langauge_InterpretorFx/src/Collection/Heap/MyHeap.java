package Collection.Heap;

import Model.Values.Value;

import java.util.Collection;
import java.util.HashMap;
import java.util.Map;
import java.util.Set;

public class MyHeap<K,V> implements MyIHeap<K,V> {
    private Map<Integer,V> map;
    private static int freePos;

    public MyHeap(){
        map= new HashMap<>();
        freePos=1;
    }

    public V getValue(K key){
        return map.get(key);
    }

    public synchronized int update(V value){
        map.put(freePos,value);
        freePos++;
        return freePos-1;
    }

    @Override
    public Iterable<Map.Entry<Integer, V>> getHeap() {
        return map.entrySet();
    }

    @Override
    public synchronized void updateExisting(int key, V value) {
        map.replace(key,value);
    }

    public String toString(){return map.toString();}
    public int size(){return map.size(); }
    public boolean isDefined(K key){
        return map.containsKey(key);
    }
    public boolean hasValue(V value){return map.containsValue(value);}
    public void remove(K key){map.remove(key);}
    public Collection<V> values(){return  map.values();}
    public Set<Integer> keySet(){return map.keySet();}

    @Override
    public void setContent(Map<Integer, V> map) {
        this.map=map;
    }

    @Override
    public Map<Integer, V> getContent() {
        return map;
    }
}
