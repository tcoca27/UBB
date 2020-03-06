package Model.Stament;

import Collection.Dictionary.MyIDictionary;
import Collection.Stack.MyIStack;
import Collection.Stack.MyStack;
import Exceptions.MyException;
import Model.Expressions.Exp;
import Model.PrgState;
import Model.Types.StringType;
import Model.Types.Type;
import Model.Values.StringValue;
import Model.Values.Value;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class openRFile implements IStmt {
    Exp exp;

    public openRFile(Exp exp){
        this.exp=exp;
    }

    public String toString(){
        return "open("+exp.toString()+")";
    }

    public PrgState execute(PrgState prg) throws MyException{
        MyIStack<IStmt> stack=prg.getStk();
        MyIDictionary<String, Value> symTbl=prg.getSymTable();
        MyIDictionary<StringValue, BufferedReader> fileTable=prg.getFileTable();
        Value v=exp.eval(symTbl,prg.getHeap());
        Type typ=v.getType();
        if(typ.equals(new StringType())){
            if(!(fileTable.isDefined((StringValue) v))){
                try {
                    BufferedReader br = new BufferedReader(new FileReader(((StringValue) v).getValue()));
                    fileTable.update((StringValue) v,br);
                }
                catch (IOException e){
                    System.out.println(e.getMessage());
                }
            }
            else throw new MyException("File is already opened");
        }
        else{
            throw new MyException("wrong type of file to open");
        }
        return null;
    }

    @Override
    public MyIDictionary<String, Type> typecheck(MyIDictionary<String, Type> typeEnv) throws MyException {
        Type t=exp.typecheck(typeEnv);
        if(t.equals(new StringType()))
            return typeEnv;
        else throw new MyException("cant open file because exp is not string");
    }
}
