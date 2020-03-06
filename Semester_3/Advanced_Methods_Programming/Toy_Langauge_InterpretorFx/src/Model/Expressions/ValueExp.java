package Model.Expressions;

import Collection.Dictionary.MyIDictionary;
import Collection.Heap.MyIHeap;
import Exceptions.MyException;
import Model.Types.Type;
import Model.Values.Value;

public class ValueExp implements Exp {
    private Value e;

    public ValueExp(Value v){
        e=v;
    }

    public Value eval(MyIDictionary<String,Value> tbl, MyIHeap<Integer,Value> heap)throws MyException {
        return e;
    }

    @Override
    public Type typecheck(MyIDictionary<String, Type> typeEnv) throws MyException {
        return e.getType();
    }

    public String toString(){
        return e.toString();
    }
}
