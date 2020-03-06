package Model.Types;

import Model.Values.StringValue;
import Model.Values.Value;

public class StringType implements Type {
    public boolean equals(Object other){
        return other instanceof StringType;
    }

    @Override
    public Value defaultVal() {
        return new StringValue("");
    }

    public String toString(){return "string";}
}
