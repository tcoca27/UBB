package SymbolTbl;

import java.util.List;

public class SymbolTbl {
    private HashTbl hashTbl;

    public SymbolTbl(){
        hashTbl = new HashTbl();
    }

    public void add(String value) {
        hashTbl.add(value);
    }

    public List<Integer> getId (String value) {
        return hashTbl.getId(value);
    }


}
