package Model;

import Collection.Dictionary.MyDictionary;
import Collection.Dictionary.MyIDictionary;
import Collection.Heap.MyHeap;
import Collection.Heap.MyIHeap;
import Collection.LTable.MyILTable;
import Collection.LTable.MyLTable;
import Collection.MyIList.MyIList;
import Collection.MyIList.MyList;
import Collection.Stack.MyIStack;
import Collection.Stack.MyStack;
import Exceptions.MyException;
import Model.Stament.IStmt;
import Model.Types.Type;
import Model.Values.StringValue;
import Model.Values.Value;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.util.concurrent.atomic.AtomicInteger;

public class PrgState {
    private MyIStack<IStmt> exeStack;
    private MyIDictionary<String, Value> symTable;
    private MyIDictionary<StringValue, BufferedReader> fileTable;
    private MyIList<Value> out;
    private IStmt originalProgram;
    private MyIHeap<Integer,Value> heap;
    private Integer id;
    private static AtomicInteger id_thread;
    private MyILTable<Integer,Integer> latchTable;

    public synchronized  AtomicInteger getId_thread() {
        return id_thread;
    }

    public synchronized  void setId_thread(AtomicInteger id_thread) {
        this.id_thread = id_thread;
    }

    public  void setId(int id) {
        this.id = id;
    }

    public  int getId() {
        return id;
    }

    public MyIStack<IStmt> getStk(){
        return exeStack;
    }

    public MyIHeap<Integer,Value> getHeap(){return heap;}

    public MyIDictionary<String,Value> getSymTable(){
        return symTable;
    }

    public MyIList<Value> getOut(){
        return out;
    }

    public MyILTable<Integer,Integer> getLatchTable() {
        return latchTable;
    }

    public MyIDictionary<StringValue,BufferedReader> getFileTable(){return fileTable;}

    public void setFileTable(MyIDictionary<StringValue,BufferedReader> ft){fileTable=ft;}

    public void setHeap(MyIHeap<Integer,Value> heap){this.heap=heap;}

    public void setExeStack(MyIStack<IStmt> exStack){
        exeStack=exStack;
    }

    public void setSymTable(MyIDictionary<String, Value> symTable) {
        this.symTable = symTable;
    }

    public void setOut(MyIList<Value> out) {
        this.out = out;
    }

    public void setLatchTable(MyILTable latchTable) {
        this.latchTable = latchTable;
    }

    public void setOriginalProgram(IStmt originalProgram) {
        this.originalProgram = originalProgram;
    }

    public PrgState(MyIList<Value> out, MyIStack<IStmt> stk, MyIDictionary<String,Value> symTbl,MyIDictionary<StringValue,BufferedReader>fileTab,MyIHeap<Integer,Value> hep, IStmt prg, int i, MyILTable<Integer,Integer> ltb) throws MyException {
        exeStack=stk;
        symTable=symTbl;
        this.out=out;
        fileTable=fileTab;
        heap=hep;
        originalProgram=prg;
        latchTable=ltb;
        stk.push(prg);
        id=i;
        id_thread= new AtomicInteger(id+1);
    }

    public PrgState(IStmt prg) throws MyException {
        MyIDictionary<String, Type> typeEnv=new MyDictionary<>();
        prg.typecheck(typeEnv);
        symTable=new MyDictionary<>();
        exeStack=new MyStack<>();
        out=new MyList<>();
        fileTable=new MyDictionary<>();
        heap=new MyHeap<>();
        latchTable=new MyLTable<>();
        originalProgram=prg;
        exeStack.push(prg);
        id=1;
        id_thread=new AtomicInteger(2);
    }

    public boolean isNotCompleted(){ return !(exeStack.isEmpty()); }

    public PrgState oneStep() throws MyException {
        if(exeStack.isEmpty())throw new MyException("No program to run");
        IStmt crtStmt=exeStack.pop();
        return crtStmt.execute(this);
    }

    @Override
    public String toString(){
        return "Program ID is "+Integer.toString(id)+"\n"+
                "---ExeStack--- \n"+exeStack.toString()+"\n"+
                "---SymTable--- \n"+symTable.toString()+"\n"+
                "---OutList--- \n"+out.toString()+"\n"+
                "---Heap---- \n"+heap.toString()+"\n"+
                "---FileTable--- \n"+fileTable.toString()+"\n\n\n";
    }
}
