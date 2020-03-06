package Collection.Heap;

import Model.Values.Value;

import java.util.Collection;
import java.util.Map;
import java.util.Set;

public interface MyIHeap<K,V> {
    V getValue (K key);
    int update(V value);
    void updateExisting(int key,V value);
    String toString();
    int size();
    boolean isDefined(K key);
    boolean hasValue(V value);
    void remove(K key);
    Collection<V> values();
    Set<Integer> keySet();
    void setContent(Map<Integer, V> map);
    Iterable<Map.Entry<Integer,V>> getHeap();
    Map<Integer,V> getContent();
}
