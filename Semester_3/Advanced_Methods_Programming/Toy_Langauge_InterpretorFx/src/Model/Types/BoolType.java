package Model.Types;

import Model.Values.BoolValue;
import Model.Values.Value;

public class BoolType implements Type {
    public boolean equals(Object other){
        return other instanceof BoolType;
    }

    @Override
    public Value defaultVal() {
        return new BoolValue(false);
    }

    public String toString(){return "bool";}
}
