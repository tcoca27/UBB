package Model.Values;

import Model.Types.IntType;
import Model.Types.Type;

public class IntValue implements Value {
    private int val;

    public IntValue(int v){
        val=v;
    }

    public int  getVal(){return val;}

    public boolean equals(Object object){
        if(object instanceof IntValue){
            return(((IntValue) object).getVal()==this.getVal());
        }
        return false;
    }

    public String toString(){
        return Integer.toString(val);
    }

    public Type getType(){
        return  new IntType();
    }
}
