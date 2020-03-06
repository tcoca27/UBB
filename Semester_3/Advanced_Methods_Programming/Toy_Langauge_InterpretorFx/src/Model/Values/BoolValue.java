package Model.Values;

import Model.Types.BoolType;
import Model.Types.Type;

public class BoolValue implements Value {
    private boolean bool;

    public BoolValue(boolean bool){
        this.bool=bool;
    }

    public boolean equals(Object object){
        if(object instanceof BoolValue)
            return(((BoolValue) object).getVal()==(this.getVal()));
        return false;
    }

    public boolean getVal(){
        return bool;
    }

    public String toString(){
        return Boolean.toString(bool);
    }

    public Type getType(){
        return new BoolType();
    }
}
