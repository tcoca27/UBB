package Model.Stament;

import Collection.Dictionary.MyIDictionary;
import Collection.Heap.MyIHeap;
import Collection.Stack.MyIStack;
import Exceptions.MyException;
import Model.Expressions.Exp;
import Model.PrgState;
import Model.Values.Value;
import Model.Types.Type;

import java.time.temporal.ValueRange;

public class AssignStmt implements IStmt{
    private String id;
    private Exp exp;

    public AssignStmt(String str, Exp e){
        id=str;
        exp=e;
    }

    public String toString(){
        return id+"="+exp.toString();
    }

    @Override
    public PrgState execute(PrgState state) throws MyException{
        MyIStack<IStmt> stk=state.getStk();
        MyIDictionary<String, Value> symTbl=state.getSymTable();
        MyIHeap<Integer,Value> heap=state.getHeap();
        Value val=exp.eval(symTbl,heap);
        if (symTbl.isDefined(id)){
            Type typId=(symTbl.getValue(id)).getType();
            if((val.getType()).equals(typId)){
                symTbl.update(id,val);
            }
            else throw new MyException("declared type of variable "+id+" and type of  the assigned expression do not match");
        }
        else {
            throw new MyException("the used variable" +id + " was not declared before");
        }
        return null;
    }

    @Override
    public MyIDictionary<String, Type> typecheck(MyIDictionary<String, Type> typeEnv) throws MyException {
        Type typevar = typeEnv.getValue(id);
        Type typeexp=exp.typecheck(typeEnv);
        if(typevar.equals(typeexp))
            return typeEnv;
        else throw new MyException("Assignment: right hand side and left hand side have different types");
    }
}
