package Model.Stament;

import Collection.Dictionary.MyIDictionary;
import Collection.Heap.MyIHeap;
import Collection.MyIList.MyIList;
import Collection.Stack.MyIStack;
import Collection.Stack.MyStack;
import Exceptions.MyException;
import Model.Expressions.ValueExp;
import Model.PrgState;
import Model.Types.Type;
import Model.Values.IntValue;
import Model.Values.StringValue;
import Model.Values.Value;

import java.io.BufferedReader;
import java.util.concurrent.atomic.AtomicInteger;

public class forkStmt implements IStmt {
    private IStmt stmt;

    public forkStmt(IStmt st){stmt=st;}

    @Override
    public String toString() {
        return "fork("+stmt.toString()+")";
    }

    @Override
    public PrgState execute(PrgState state) throws MyException {
        MyIStack<IStmt> stk=new MyStack<>();
        AtomicInteger id=state.getId_thread();
        int i=id.intValue();
        state.setId_thread(new AtomicInteger(i+1));
        return new PrgState(state.getOut(),stk,state.getSymTable().clone(),state.getFileTable(),state.getHeap(),stmt,i,state.getLatchTable());
    }

    @Override
    public MyIDictionary<String, Type> typecheck(MyIDictionary<String, Type> typeEnv) throws MyException {
        MyIDictionary<String,Type> fork=stmt.typecheck(typeEnv);
        return typeEnv;
    }
}
