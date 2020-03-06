package Model.Stament;

import Collection.Dictionary.MyIDictionary;
import Collection.Stack.MyIStack;
import Exceptions.MyException;
import Model.Expressions.Exp;
import Model.PrgState;
import Model.Types.BoolType;
import Model.Types.Type;
import Model.Values.BoolValue;
import Model.Values.Value;

public class IfStmt implements IStmt {
    private Exp exp;
    private IStmt thenS;
    private IStmt elseS;

    public IfStmt(Exp e, IStmt t, IStmt el){
        exp=e;
        thenS=t;
        elseS=el;
    }

    public String toString(){
        return "IF("+ exp.toString()+") THEN(" +thenS.toString() +") ELSE("+elseS.toString()+")";
    }

    public PrgState execute(PrgState state) throws MyException {
        MyIStack<IStmt> stack=state.getStk();
        Value v1=exp.eval(state.getSymTable(),state.getHeap());
        if(v1.getType().equals(new BoolType())){
            BoolValue b=(BoolValue) v1;
            boolean B= b.getVal();
            if(B){
                stack.push(thenS);
            }
            else{
                stack.push(elseS);
            }
        }
        return null;
    }

    @Override
    public MyIDictionary<String, Type> typecheck(MyIDictionary<String, Type> typeEnv) throws MyException {
        Type typexp=exp.typecheck(typeEnv);
        if(typexp.equals(new BoolType())){
            MyIDictionary<String,Type> thenEnv,elseEnv;
            thenEnv=thenS.typecheck(typeEnv);
            elseEnv=elseS.typecheck(typeEnv);
            return typeEnv;
        }
        else throw new MyException("the condition of if is not bool");
    }
}
