package Model.Stament;

import Collection.Dictionary.MyIDictionary;
import Exceptions.MyException;
import Model.Expressions.Exp;
import Model.PrgState;
import Model.Types.BoolType;
import Model.Types.Type;
import Model.Values.Value;

public class CondAsg implements IStmt {
    private Exp v,exp1,exp2,exp3;

    public CondAsg(Exp v,Exp e1, Exp e2,Exp e3){
        this.v=v;
        exp1=e1;
        exp2=e2;
        exp3=e3;
    }

    @Override
    public String toString() {
        return v.toString()+"="+exp1.toString()+"?"+exp2.toString()+":"+exp3.toString();
    }

    @Override
    public PrgState execute(PrgState state) throws MyException {
        IStmt st=new IfStmt(exp1,new AssignStmt(v.toString(),exp2),new AssignStmt(v.toString(),exp3));
        state.getStk().push(st);
        return null;
    }

    @Override
    public MyIDictionary<String, Type> typecheck(MyIDictionary<String, Type> typeEnv) throws MyException {
        Type t1=exp1.typecheck(typeEnv);
        if(t1.equals(new BoolType())){
            Type t2=exp2.typecheck(typeEnv);
            Type t3=exp3.typecheck(typeEnv);
            Type vt=v.typecheck(typeEnv);
            if(vt.equals(t3)){
                if(t3.equals(t2)){
                    return typeEnv;
                }
                else throw new MyException("types don't match");
            }
            else throw new MyException("types don't match");
        }
        else throw new MyException(exp1.toString()+" not a bool type");
    }
}
