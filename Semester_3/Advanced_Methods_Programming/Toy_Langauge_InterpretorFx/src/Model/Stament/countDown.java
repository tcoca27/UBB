package Model.Stament;

import Collection.Dictionary.MyDictionary;
import Collection.Dictionary.MyIDictionary;
import Collection.LTable.MyILTable;
import Exceptions.MyException;
import Model.PrgState;
import Model.Types.Type;
import Model.Values.IntValue;
import Model.Values.Value;

import java.util.concurrent.locks.ReentrantLock;

public class countDown implements IStmt {
    private String var;
    private static ReentrantLock lock = new ReentrantLock();

    public countDown(String v){var=v;}

    @Override
    public String toString() {
        return "countDown("+var+")";
    }

    @Override
    public PrgState execute(PrgState state) throws MyException {
        MyIDictionary<String, Value> sym = state.getSymTable();
        MyILTable<Integer,Integer> lt=state.getLatchTable();
        if (sym.isDefined(var)) {
            Value foundIndex = sym.getValue(var);
            if (foundIndex instanceof IntValue) {
                int i = ((IntValue) foundIndex).getVal();
                if( lt.isDefined(i)){
                    if(lt.getValue(i)>0)lt.update(i,lt.getValue(i)-1);
                    state.getOut().add(new IntValue(state.getId()));
                }
                else throw new MyException(i+" not defined in latch");
            }
            else throw new MyException(foundIndex+" not an int");
        }
        else throw new MyException(var+" is not defined");
        return null;
    }

    @Override
    public MyIDictionary<String, Type> typecheck(MyIDictionary<String, Type> typeEnv) throws MyException {
        return typeEnv;
    }
}
