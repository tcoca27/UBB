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

import java.sql.Ref;


public class newV implements  IStmt{
    private String var_name;
    private Exp exp;

    public newV(String vn,Exp e1){
        var_name=vn;
        exp=e1;
    }

    @Override
    public String toString() {
        return "new("+var_name+","+exp.toString()+")";
    }

    public PrgState execute(PrgState state) throws MyException{
        MyIDictionary<String, Value> symTbl=state.getSymTable();
        MyIHeap<Integer,Value> heap=state.getHeap();
        if(symTbl.isDefined(var_name)){
            Type v=symTbl.getValue(var_name).getType();
            if(v instanceof RefType){
                Value v2=exp.eval(symTbl,heap);
                RefType r=(RefType) v;
                if(v2.getType().equals(r.getInner())){
                    int pos=heap.update(v2);
                    symTbl.update(var_name,new RefValue(v2.getType(),pos));
                }
                else throw new MyException("values don't have the same types");
            }
            else throw new MyException(var_name+" doesn't have RefType");
        }
        else throw new MyException(var_name+" not defined");
        return null;
    }

    @Override
    public MyIDictionary<String, Type> typecheck(MyIDictionary<String, Type> typeEnv) throws MyException {
        Type typevar=typeEnv.getValue(var_name);
        Type typexp=exp.typecheck(typeEnv);
        if(typevar.equals(new RefType(typexp)))
            return typeEnv;
        else throw new MyException("Assignment: right hand side and left hand side have different types ");
    }
}
