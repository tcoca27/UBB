package Model.Expressions;

import Collection.Dictionary.MyIDictionary;
import Collection.Heap.MyIHeap;
import Collection.MyIList.MyIList;
import Exceptions.MyException;
import Model.Types.RefType;
import Model.Types.Type;
import Model.Values.RefValue;
import Model.Values.Value;

import java.sql.Ref;

public class rH implements Exp {
    private Exp exp;

    public rH(Exp e){exp=e;}

    @Override
    public String toString() {
        return "rH("+exp.toString()+")";
    }

    @Override
    public Value eval(MyIDictionary<String, Value> tbl, MyIHeap<Integer, Value> heap) throws MyException {
        Value v = exp.eval(tbl, heap);
        if (v instanceof RefValue) {
            int adr = ((RefValue) v).getAddress();
            if (heap.isDefined(adr)) {
                return heap.getValue(adr);
            } else throw new MyException(Integer.toString(adr) + " not defined in heap");
        }
        else throw new MyException(exp.toString()+" is not RefValue");
    }

    @Override
    public Type typecheck(MyIDictionary<String, Type> typeEnv) throws MyException {
        Type t= exp.typecheck(typeEnv);
        if(t instanceof RefType){
            RefType reft=(RefType) t;
            return reft.getInner();
        }
        else throw new MyException("the rH argument is not a Ref Type");
    }
}
