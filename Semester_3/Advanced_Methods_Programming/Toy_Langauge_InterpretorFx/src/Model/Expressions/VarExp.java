package Model.Expressions;

import Collection.Dictionary.MyIDictionary;
import Collection.Heap.MyIHeap;
import Exceptions.MyException;
import Model.Types.Type;
import Model.Values.Value;

public class VarExp implements Exp {
    private String id;

    public VarExp(String str){
        id=str;
    }

   public Value eval(MyIDictionary<String,Value> tbl, MyIHeap<Integer,Value> heap){
       return tbl.getValue(id);
   }

    @Override
    public Type typecheck(MyIDictionary<String, Type> typeEnv) throws MyException {
        if(typeEnv.isDefined(id)) return typeEnv.getValue(id);
        else throw new MyException(id+" not defined");
    }

    public String toString(){
        return id;
   }
}
