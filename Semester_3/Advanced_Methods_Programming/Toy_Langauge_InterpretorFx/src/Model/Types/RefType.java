package Model.Types;

import Model.Values.RefValue;
import Model.Values.Value;

import java.sql.Ref;

public class RefType implements Type {
    private Type inner;
    public RefType(Type type){
        inner=type;
    }

    public Type getInner(){return inner;}

    public boolean equals(Object other){
        if(other instanceof RefType){
            return inner.equals(((RefType) other).getInner());
        }
        else return false;
    }

    public String toString(){return "Ref("+inner.toString()+")";}

    public Value defaultVal(){return new RefValue(inner,0);}

}
