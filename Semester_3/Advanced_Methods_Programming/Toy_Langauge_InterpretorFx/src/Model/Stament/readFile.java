package Model.Stament;

import Collection.Dictionary.MyIDictionary;
import Exceptions.MyException;
import Model.Expressions.Exp;
import Model.PrgState;
import Model.Types.IntType;
import Model.Types.StringType;
import Model.Types.Type;
import Model.Values.IntValue;
import Model.Values.StringValue;
import Model.Values.Value;

import java.io.BufferedReader;
import java.io.IOException;

public class readFile implements IStmt {
    private Exp exp;
    private String var_name;

    public readFile(Exp exp, String var){
        this.exp=exp;
        var_name=var;
    }

    public String toString(){
        return "read("+var_name+","+exp.toString()+")";
    }

    public PrgState execute(PrgState prg) throws MyException{
        MyIDictionary<String, Value> symTable=prg.getSymTable();
        MyIDictionary<StringValue, BufferedReader> fileTable=prg.getFileTable();
        if(symTable.isDefined(var_name)){
            Value v=symTable.getValue(var_name);
            if(v.getType().equals(new IntType())){
                Value v2=exp.eval(symTable,prg.getHeap());
                if(v2.getType().equals(new StringType())){
                    if(fileTable.isDefined((StringValue) v2)){
                        BufferedReader br=fileTable.getValue((StringValue) v2);
                        try {
                            String read=br.readLine();
                            IntValue val;
                            if(read==null){
                                val=new IntValue(0);
                            }
                            else{
                                val=new IntValue(Integer.parseInt(read));
                            }
                            symTable.update(var_name,val);
                        }
                        catch (IOException e){
                            System.out.println(e.getMessage());
                        }
                    }
                    else throw new MyException("expression is not defined in the file table");
                }
                else throw new MyException("Expression is not a string type");
            }
            else throw new MyException("value of "+var_name+" is not an int");
        }
        else throw new MyException(var_name+" is not defined in the symbol table");
        return null;
    }

    @Override
    public MyIDictionary<String, Type> typecheck(MyIDictionary<String, Type> typeEnv) throws MyException {
        Type t=exp.typecheck(typeEnv);
        Type t2=typeEnv.getValue(var_name);
        if(t.equals(new StringType()))
            if(t2.equals(new IntType()))
                return typeEnv;
            else throw new MyException(var_name+ " is not an int");
        else throw new MyException("cant read file because exp is not string");
    }
}
