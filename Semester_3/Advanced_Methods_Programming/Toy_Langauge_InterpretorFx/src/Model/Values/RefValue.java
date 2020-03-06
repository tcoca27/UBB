package Model.Values;

import Model.Types.RefType;
import Model.Types.Type;

public class RefValue implements Value {
    private int address;
    private Type locationType;

    public RefValue(Type type,int addr){
        locationType=type;
        address=addr;
    }

    public Type getLocationType(){return locationType;}

    public int getAddress(){return address;}

    public boolean equals(Object other){
        if(other instanceof RefValue){
            return(address==((RefValue) other).getAddress() && locationType.equals(((RefValue) other).getType()));
        }
        return false;
    }

    @Override
    public String toString() {
        return "("+Integer.toString(address)+","+locationType.toString()+")";
    }

    public Type getType(){return new RefType(locationType); }

}
