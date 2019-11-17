package model.collections.dictionary;

import java.util.HashMap;
import java.util.Map;
import java.util.stream.Collectors;

public class Dictionary<K, V> implements IDictionary<K,V> {
    private Map<K, V> map = new HashMap<>();

    @Override
    public V lookup(K key)
    {
        return map.get(key);
    }

    @Override
    public void put(K key, V value)
    {
        map.put(key, value);
    }

    @Override
    public boolean exists(K key)
    {
        return map.containsKey(key);
    }

    @Override
    public void delete(K key)
    {
        map.remove(key);
    }

    @Override
    public String toString()
    {
        return map.entrySet().stream()
                .map(x -> x.getKey().toString() + " -> " + x.getValue().toString())
                .collect(Collectors.joining("\n"));
    }
}
