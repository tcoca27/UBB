package Collection.LTable;


import java.util.Collection;
import java.util.Map;
import java.util.Set;

public interface MyILTable<K,V> {
    V getValue (K key);
    void update(K key,V value);
    String toString();
    int size();
    boolean isDefined(K key);
    boolean hasValue(V value);
    void remove(K key);
    Collection<V> values();
    Set<K> keySet();
    Map<K,V> getContent();
    Iterable<Map.Entry<K,V>> getDict();
    MyILTable<K,V> clone();
    Set<K> getKeys();
}
