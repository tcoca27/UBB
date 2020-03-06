package Model.Expressions;

import Collection.Dictionary.MyIDictionary;
import Collection.Heap.MyIHeap;
import Exceptions.MyException;
import Model.Types.BoolType;
import Model.Types.IntType;
import Model.Types.Type;
import Model.Values.BoolValue;
import Model.Values.IntValue;
import Model.Values.Value;

public class RelExp implements Exp {
    private Exp exp1;
    private Exp exp2;
    private String operator;

    public RelExp(Exp e1,Exp e2,String operator){
        exp1=e1;
        exp2=e2;
        this.operator=operator;
    }

    public String toString(){
        return exp1.toString()+operator+exp2.toString();
    }

    public Value eval(MyIDictionary<String,Value> symTbl, MyIHeap<Integer,Value> heap) throws MyException {
        Value v1,v2;
        v1=exp1.eval(symTbl,heap);
        if(v1.getType().equals(new IntType())){
            v2=exp2.eval(symTbl,heap);
            if(v2.getType().equals(new IntType())){
                IntValue i1=(IntValue) v1;
                IntValue i2=(IntValue) v2;
                int n1,n2;
                n1=i1.getVal();
                n2=i2.getVal();
                switch (operator){
                    case "<":
                        if(n1<n2)return new BoolValue(true);
                        else return new BoolValue(false);
                    case "<=":
                        if(n1<=n2)return new BoolValue(true);
                        else return new BoolValue(false);
                    case "==":
                        if(n1==n2)return new BoolValue(true);
                        else return new BoolValue(false);
                    case ">":
                        if(n1>n2)return new BoolValue(true);
                        else return new BoolValue(false);
                    case ">=":
                        if(n1>=n2)return new BoolValue(true);
                        else return new BoolValue(false);
                    case "!=":
                        if(n1!=n2)return new BoolValue(true);
                        else return new BoolValue(false);
                    default:
                        throw new MyException(operator+" is not a valid operator");
                }
            }
            else throw new MyException(exp2.toString()+" is not int");
        }
         throw new MyException(exp1.toString()+" is not int");
    }

    @Override
    public Type typecheck(MyIDictionary<String, Type> typeEnv) throws MyException {
        Type t1,t2;
        t1=exp1.typecheck(typeEnv);
        t2=exp2.typecheck(typeEnv);
        if(t1.equals(new IntType())){
            if(t2.equals(new IntType())){
                return new BoolType();
            }
            else throw new MyException("second operand not integer");
        }
        else throw new MyException("first operand not integer");
    }
}
