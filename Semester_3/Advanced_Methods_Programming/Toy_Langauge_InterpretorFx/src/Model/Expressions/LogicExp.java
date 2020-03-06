package Model.Expressions;

import Collection.Dictionary.MyIDictionary;
import Collection.Heap.MyIHeap;
import Exceptions.MyException;
import Model.Types.BoolType;
import Model.Types.Type;
import Model.Values.BoolValue;
import Model.Values.Value;

public class LogicExp implements Exp {
    private Exp e1;
    private Exp e2;
    private int op; //1:and  2:or

    public Value eval(MyIDictionary<String,Value> tbl, MyIHeap<Integer,Value> heap) throws MyException {
        Value v1,v2;
        v1=e1.eval(tbl,heap);
        if(v1.getType().equals(new BoolType())){
            v2=e2.eval(tbl,heap);
            if(v2.getType().equals(new BoolType())){
                BoolValue b1= (BoolValue)v1;
                BoolValue b2= (BoolValue)v2;
                boolean b11,b22;
                b11=((BoolValue) b1).getVal();
                b22=((BoolValue) b2).getVal();
                if(op==1)return new BoolValue(b11 && b22);
                else if(op==2)return new BoolValue(b11 || b22);
                else throw new MyException("wrong operator");
            }
            else throw new MyException("Second operand is not of type bool");
        }
        else throw new MyException("First operand is not bool");
    };

    public String toString(){
        if(op==1) return e1.toString()+"&&"+e2.toString();
        else return e1.toString()+"||"+e2.toString();
    }

    @Override
    public Type typecheck(MyIDictionary<String, Type> typeEnv) throws MyException {
        Type t1, t2;
        t1=e1.typecheck(typeEnv);
        t2=e2.typecheck(typeEnv);
        if(t1.equals(new BoolType())){
            if(t2.equals(new BoolType())){
                return new BoolType();
            }
            else throw new MyException("second operand not bool");
        }
        else throw new MyException("first operand not bool");
    }
}
