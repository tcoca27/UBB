package Collection.Dictionary;

import java.util.*;

public class MyDictionary<K,V> implements MyIDictionary<K,V> {
    private Map<K,V> dictionary;

    public MyDictionary(){
        dictionary=new HashMap<>();
    }

    public V getValue(K key){
        return dictionary.get(key);
    }

    public synchronized void update(K key,V value){
        if(isDefined(key))dictionary.replace(key,value);
        else dictionary.put(key,value);
    }
    public String toString(){return dictionary.toString();}
    public int size(){return dictionary.size(); }
    public boolean isDefined(K key){
        return dictionary.containsKey(key);
    }
    public boolean hasValue(V value){return dictionary.containsValue(value);}
    public void remove(K key){dictionary.remove(key);}
    public Collection<V> values(){return  dictionary.values();}
    public Set<K> keySet(){return dictionary.keySet();}

    @Override
    public Map<K, V> getContent() {
        return dictionary;
    }

    @Override
    public Iterable<Map.Entry<K, V>> getDict() {
        return dictionary.entrySet();
    }

    @Override
    public Set<K> getKeys() {
        return dictionary.keySet();
    }

    public MyIDictionary<K,V> clone(){
        MyIDictionary<K,V>dict= new MyDictionary<>();
        this.getContent().forEach((K,V)->{dict.update(K,V);});
        return dict;
    }
}
