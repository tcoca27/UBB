package Model.Stament;

import Collection.Dictionary.MyIDictionary;
import Exceptions.MyException;
import Model.PrgState;
import Model.Types.Type;
import Model.Values.Value;

public class VarDeclStmt implements IStmt {
    private String id;
     private Type type;

    public VarDeclStmt(String str, Type typ){
        id=str;
        type=typ;
    }

    @Override
    public String toString() {
        return type.toString()+" "+id;
    }

    @Override
    public PrgState execute(PrgState state) throws MyException{
        MyIDictionary<String, Value> symTbl=state.getSymTable();
        if(symTbl.isDefined(id))throw new MyException(id+" already defined");
        else{
            symTbl.update(id,type.defaultVal());
        }
        return null;
    }

    @Override
    public MyIDictionary<String, Type> typecheck(MyIDictionary<String, Type> typeEnv) throws MyException {
        MyIDictionary<String,Type> newEnv=typeEnv.clone();
        newEnv.update(id,type);
        return newEnv;
    }
}
