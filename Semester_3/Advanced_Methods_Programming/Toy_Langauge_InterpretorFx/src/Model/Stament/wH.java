package Model.Stament;

import Collection.Dictionary.MyIDictionary;
import Collection.Heap.MyIHeap;
import Exceptions.MyException;
import Model.Expressions.Exp;
import Model.PrgState;
import Model.Types.RefType;
import Model.Types.Type;
import Model.Values.RefValue;
import Model.Values.Value;

public class wH implements IStmt {
    private String var_name;
    private Exp exp;

    public wH(String vn, Exp e1){exp=e1;var_name=vn;}

    @Override
    public String toString() {
        return "wH("+var_name+","+exp.toString()+")";
    }

    @Override
    public PrgState execute(PrgState state) throws MyException {
        MyIDictionary<String, Value> symTbl=state.getSymTable();
        MyIHeap<Integer, Value> heap=state.getHeap();
        if(symTbl.isDefined(var_name)){
            Value v1=symTbl.getValue(var_name);
            if(v1.getType() instanceof RefType){
                int adr=((RefValue)v1).getAddress();
                if(heap.isDefined(adr)){
                    Value v2=exp.eval(symTbl,heap);
                    if(v2.getType().equals(((RefValue)v1).getLocationType())){
                        heap.updateExisting(adr,v2);
                    }
                    else throw new MyException("Types dont match");
                }
                else throw new MyException("key not defined in heap");
            }
            else throw new MyException(var_name+" is not RefType");
        }
        else throw new MyException(var_name+" is not defined");
        return null;
    }

    @Override
    public MyIDictionary<String, Type> typecheck(MyIDictionary<String, Type> typeEnv) throws MyException {
        Type t1,t2;
        t1=exp.typecheck(typeEnv);
        t2=typeEnv.getValue(var_name);
        if(t2.equals(new RefType(t1)))
            return typeEnv;
        else throw new MyException("exp and ref have different types");
    }
}
