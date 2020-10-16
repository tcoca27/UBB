package SymbolTbl;

import jdk.internal.joptsimple.util.KeyValuePair;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class HashTbl {
    public Map<Integer, List<String>> table;

    public HashTbl() {
        table = new HashMap<>();
    }

    private int hashCode(String value) {
        int sum = 0;
        for (char c : value.toCharArray()) {
            sum += c;
        }
        return sum % 256; //todo change to constant
    }

    public ArrayList<String> search(String value) {
        int hash = hashCode(value);
        return (ArrayList<String>) table.getOrDefault(hash, null);
    }

    @Override
    public String toString() {
        return "SymbolTbl{" +
                "symbols=" + table +
                '}';
    }

    public void add(String value) {
        List<String> colidedList = new ArrayList<>();
        if (search(value) != null) {
            colidedList = search(value);
            if (colidedList.contains(value)){
                System.out.println("Value is already in table");
            }
            else {
                colidedList.add(value);
            }
        }
        else {
            table.put(hashCode(value), colidedList);
        }
    }

    public List<Integer> getId(String value) {
        List<String> colidedList = new ArrayList<>();
        if (search(value) != null) {
            colidedList = search(value);
            if (colidedList.contains(value)){
                List<Integer> pair = new ArrayList<>();
                pair.add(hashCode(value));
                pair.add(colidedList.indexOf(value));
                return pair;
            }
        }
        return null;
    }
}