package Model.Stament;

import Collection.Dictionary.MyIDictionary;
import Collection.Heap.MyIHeap;
import Exceptions.MyException;
import Model.Expressions.Exp;
import Model.PrgState;
import Model.Types.StringType;
import Model.Types.Type;
import Model.Values.StringValue;
import Model.Values.Value;

import java.io.BufferedReader;
import java.io.IOException;

public class closeRFile implements IStmt {
    private Exp exp;

    public closeRFile(Exp exp){
        this.exp=exp;
    }

    public String toString(){
        return "close("+exp.toString()+")";
    }

    public PrgState execute(PrgState prg) throws MyException {
        MyIDictionary<String ,Value> symTbl=prg.getSymTable();
        MyIDictionary<StringValue, BufferedReader> fileTable=prg.getFileTable();
        MyIHeap<Integer,Value> heap=prg.getHeap();
        Value v=exp.eval(symTbl,heap);
        if(v.getType().equals(new StringType())){
            if(fileTable.isDefined((StringValue) v)){
                BufferedReader bf=fileTable.getValue((StringValue) v);
                try {
                    bf.close();
                }
                catch (IOException e){
                    System.out.println(e.getMessage());
                }
                fileTable.remove((StringValue) v);
            }
            else throw new MyException(v.toString()+" is not defined in the file table");
        }
        else throw new MyException("Value of expression "+exp.toString()+" is not a string");
        return null;
    }

    @Override
    public MyIDictionary<String, Type> typecheck(MyIDictionary<String, Type> typeEnv) throws MyException {
        Type t=exp.typecheck(typeEnv);
        if(t.equals(new StringType()))
            return typeEnv;
        else throw new MyException("exp is not a string");
    }
}
