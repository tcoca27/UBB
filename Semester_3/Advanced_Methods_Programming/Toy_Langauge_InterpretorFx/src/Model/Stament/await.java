package Model.Stament;

import Collection.Dictionary.MyIDictionary;
import Exceptions.MyException;
import Model.PrgState;
import Model.Types.Type;
import Model.Values.IntValue;
import Model.Values.Value;

public class await implements IStmt {
    private String var;

    public await(String v){var=v;}

    @Override
    public String toString() {
        return "await("+var+")";
    }

    @Override
    public PrgState execute(PrgState state) throws MyException {
        MyIDictionary<String, Value> sym=state.getSymTable();
        if(sym.isDefined(var)){
            Value foundIndex=sym.getValue(var);
            if(foundIndex instanceof IntValue){
                int i=((IntValue) foundIndex).getVal();
                if(state.getLatchTable().isDefined(i)){
                    int res=state.getLatchTable().getValue(i);
                    if(res==0)return null;
                    else{
                        state.getStk().push(this);
                    }
                }
                else throw new MyException(i+" not defined in latch");
            }
            else throw new MyException(foundIndex+ " not int");
        }
        else throw new MyException(var+ "not defined");
        return null;
    }

    @Override
    public MyIDictionary<String, Type> typecheck(MyIDictionary<String, Type> typeEnv) throws MyException {
        return null;
    }
}
