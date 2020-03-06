package Model.Stament;

import Collection.Dictionary.MyIDictionary;
import Exceptions.MyException;
import Model.PrgState;
import Model.Types.Type;

public interface IStmt {
    PrgState execute(PrgState state) throws MyException; //which is the execution method for a statement.
    MyIDictionary<String, Type> typecheck(MyIDictionary<String,Type> typeEnv)throws MyException;
}
