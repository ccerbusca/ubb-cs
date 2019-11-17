package model.collections.dictionary;

public interface IDictionary<K, V> {
    V lookup(K key);
    void put(K key, V value);
    boolean exists(K key);
    void delete(K key);
}
