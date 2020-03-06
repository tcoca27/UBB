package Model.Types;

import Model.Values.IntValue;
import Model.Values.Value;

public class IntType implements Type {
    public boolean equals(Object other){
        return other instanceof IntType;
    }

    @Override
    public Value defaultVal() {
        return new IntValue(0);
    }

    public String toString(){return "int";}
}
