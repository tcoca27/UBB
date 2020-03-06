package Model.Stament;

import Collection.Dictionary.MyIDictionary;
import Collection.Heap.MyIHeap;
import Collection.MyIList.MyIList;
import Collection.Stack.MyIStack;
import Exceptions.MyException;
import Model.Expressions.Exp;
import Model.PrgState;
import Model.Types.BoolType;
import Model.Types.Type;
import Model.Values.BoolValue;
import Model.Values.Value;

public class While implements IStmt {
    private Exp exp;
    private IStmt st;

    public While(Exp e,IStmt s){exp=e;st=s;}

    @Override
    public String toString() {
        return "while("+exp.toString()+")"+st.toString();
    }

    //??
    @Override
    public PrgState execute(PrgState state) throws MyException {
        MyIDictionary<String,Value>symTbl=state.getSymTable();
        MyIHeap<Integer,Value>heap=state.getHeap();
        MyIStack<IStmt> stack=state.getStk();
        Value v1=exp.eval(symTbl,heap);
        if(v1 instanceof BoolValue) {
            BoolValue b = (BoolValue) v1;
            if (b.getVal()) {
                stack.push(this);
                stack.push(st);
            }
        }
        else throw new MyException("expression is not boolType");
        return null;
    }

    @Override
    public MyIDictionary<String, Type> typecheck(MyIDictionary<String, Type> typeEnv) throws MyException {
        Type t=exp.typecheck(typeEnv);
        if(t.equals(new BoolType())){
            MyIDictionary<String,Type> whiletc=st.typecheck(typeEnv);
            return typeEnv;
        }
        else throw new MyException("while exp is not a bool type");
    }
}

