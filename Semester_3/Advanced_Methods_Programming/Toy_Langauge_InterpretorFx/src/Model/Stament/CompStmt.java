package Model.Stament;

import Collection.Dictionary.MyIDictionary;
import Exceptions.MyException;
import Model.PrgState;
import Collection.Stack.MyIStack;
import Model.Types.Type;

public class CompStmt implements IStmt {
    private IStmt first;
    private IStmt snd;

    public CompStmt(IStmt f, IStmt s){
        first=f;
        snd=s;
    }

    public String toString(){
        return "("+first.toString()+";"+snd.toString()+")";
    }

    public PrgState execute(PrgState state){
        MyIStack<IStmt> stk=state.getStk();
        stk.push(snd);
        stk.push(first);
        return null;
    }

    @Override
    public MyIDictionary<String, Type> typecheck(MyIDictionary<String, Type> typeEnv) throws MyException {
        return snd.typecheck(first.typecheck(typeEnv));
    }
}
