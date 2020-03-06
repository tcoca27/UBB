package Collection.LTable;

import java.util.Collection;
import java.util.HashMap;
import java.util.Map;
import java.util.Set;
import java.util.concurrent.locks.ReentrantLock;

public class MyLTable<K,V> implements MyILTable<K,V> {
    private Map<K,V> table;

    public MyLTable(){table=new HashMap<>();}

    @Override
    public synchronized V getValue(K key){
        return table.get(key);
    }

    public synchronized void update(K key,V value){
        if(isDefined(key))table.replace(key,value);
        else table.put(key,value);
    }
    public String toString(){return table.toString();}
    public int size(){return table.size(); }
    public boolean isDefined(K key){
        return table.containsKey(key);
    }
    public boolean hasValue(V value){return table.containsValue(value);}
    public void remove(K key){table.remove(key);}
    public Collection<V> values(){return  table.values();}
    public Set<K> keySet(){return table.keySet();}

    public Map<K, V> getContent() {
        return table;
    }
    public Iterable<Map.Entry<K, V>> getDict() {
        return table.entrySet();
    }
    public Set<K> getKeys() {
        return table.keySet();
    }
    public MyILTable<K,V> clone(){
        MyILTable<K,V>dict= new MyLTable<>();
        this.getContent().forEach((K,V)->{dict.update(K,V);});
        return dict;
    }
}
