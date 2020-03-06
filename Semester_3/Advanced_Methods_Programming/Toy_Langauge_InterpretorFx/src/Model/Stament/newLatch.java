package Model.Stament;

import Collection.Dictionary.MyIDictionary;
import Exceptions.MyException;
import Model.Expressions.Exp;
import Model.PrgState;
import Model.Types.IntType;
import Model.Types.Type;
import Model.Values.IntValue;
import Model.Values.Value;

import java.util.concurrent.locks.ReentrantLock;

public class newLatch implements IStmt {
    private String var;
    private Exp exp;
    private static int freeloc=-1;
    private static ReentrantLock lock = new ReentrantLock();


    public newLatch(String v, Exp e){var=v; exp=e;}

    @Override
    public String toString() {
        return "newLatch("+var+","+exp.toString()+")";
    }

    @Override
    public PrgState execute(PrgState state) throws MyException {
        Value v=exp.eval(state.getSymTable(),state.getHeap());
        if(!(v instanceof IntValue))throw new MyException(exp.toString()+" not an int");
        else{
            lock.lock();
            int i=((IntValue) v).getVal();
            state.getLatchTable().update(freeloc,i);
            if(state.getSymTable().isDefined(var)){
                Value vvar=state.getSymTable().getValue(var);
                if(vvar instanceof IntValue){
                    state.getSymTable().update(var,new IntValue(freeloc));
                }
                else throw new MyException(var+"is not int");
            }
            else throw new MyException(var+"is not defined");
            lock.unlock();
        }
        return null;
    }

    @Override
    public MyIDictionary<String, Type> typecheck(MyIDictionary<String, Type> typeEnv) throws MyException {
        Type v=typeEnv.getValue(var);
        if(!(v instanceof IntType))throw new MyException(var+" not an int");
        Type v2= exp.typecheck(typeEnv);
        if(!(v2 instanceof IntType))throw new MyException(exp.toString()+" not an int");
        return typeEnv;
    }
}
