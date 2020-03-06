package Model.Values;

import Model.Types.StringType;
import Model.Types.Type;

public class StringValue implements Value {
    private String string;

    public StringValue(String str){string=str;}

    public String getValue(){return string;}

    public String toString(){return string;}

    public boolean equals(Object object){
        if(object instanceof StringValue){
            return (((StringValue) object).getValue().equals(this.getValue()));
        }
        return false;
    }

    @Override
    public Type getType() {
        return new StringType();
    }
}
