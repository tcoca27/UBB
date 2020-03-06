import Collection.Dictionary.MyDictionary;
import Collection.Dictionary.MyIDictionary;
import Collection.Heap.MyHeap;
import Collection.Heap.MyIHeap;
import Collection.MyIList.MyIList;
import Collection.MyIList.MyList;
import Collection.Stack.MyIStack;
import Collection.Stack.MyStack;
import Controller.Controller;
import Exceptions.MyException;
import Model.Expressions.*;
import Model.PrgState;
import Model.Stament.*;
import Model.Types.BoolType;
import Model.Types.IntType;
import Model.Types.RefType;
import Model.Types.StringType;
import Model.Values.BoolValue;
import Model.Values.IntValue;
import Model.Values.StringValue;
import Model.Values.Value;
import Repository.IRepository;
import Repository.Repository;
import View.ExitCommand;
import View.RunExample;
import View.TextMenu;
import javafx.application.Application;
import javafx.stage.Stage;

import java.io.BufferedReader;

public class Main extends Application {

    @Override
    public void start(Stage primaryStage) throws Exception {
        IRepository repository1= new Repository("log1.txt");
        IRepository repository2= new Repository("log2.txt");
        IRepository repository3= new Repository("log3.txt");
        IRepository repository4= new Repository("log4.txt");
        IRepository repository5= new Repository("log5.txt");
        IRepository repository6= new Repository("log6.txt");
        IRepository repository7= new Repository("log7.txt");
        IRepository repository8= new Repository("log8.txt");
        IRepository repository9= new Repository("log9.txt");
        IRepository repository10= new Repository("log10.txt");
        IRepository repository11= new Repository("log11.txt");
        IRepository repository12= new Repository("log12.txt");
        IRepository repository13= new Repository("log13.txt");

        IStmt ex1= new CompStmt(new VarDeclStmt("v",new IntType()),
                new CompStmt(new AssignStmt("v",new ValueExp(new IntValue(2))), new PrintStmt(new VarExp("v"))));
        IStmt ex2 = new CompStmt( new VarDeclStmt("a",new IntType()),  new CompStmt(new VarDeclStmt("b",new IntType()),
                new CompStmt(new AssignStmt("a", new ArithExp('+',new ValueExp(new IntValue(2)),
                        new ArithExp('*',new ValueExp(new IntValue(3)), new ValueExp(new IntValue(5))))),
                        new CompStmt(new AssignStmt("b",new ArithExp('+',new VarExp("a"), new ValueExp(new IntValue(1)))),
                                new PrintStmt(new VarExp("b"))))));
        IStmt ex3 = new CompStmt(new VarDeclStmt("a",new BoolType()),new CompStmt(new VarDeclStmt("v", new IntType()),
                new CompStmt(new AssignStmt("a", new ValueExp(new BoolValue(true))),new CompStmt(new IfStmt(new VarExp("a"),
                        new AssignStmt("v",new ValueExp(new IntValue(2))), new AssignStmt("v", new ValueExp(new IntValue(3)))),
                        new PrintStmt(new VarExp("v"))))));
        IStmt ex4=new CompStmt(new VarDeclStmt("varf",new StringType()),new CompStmt(new AssignStmt("varf",new ValueExp(new StringValue("test.in"))),
                new CompStmt(new openRFile(new VarExp("varf")),new CompStmt(new VarDeclStmt("varc",new IntType()),new CompStmt(new
                        readFile(new VarExp("varf"),"varc"),new CompStmt(new PrintStmt(new VarExp("varc")), new
                        CompStmt(new readFile(new VarExp("varf"),"varc"),new CompStmt(new PrintStmt(new VarExp("varc")), new
                        closeRFile(new VarExp("varf"))))))))));
        IStmt ex5=new CompStmt(new VarDeclStmt("v",new IntType()),new CompStmt(new AssignStmt("v",new ValueExp(new IntValue(4))),
                new CompStmt(new While(new RelExp(new VarExp("v"),new ValueExp(new IntValue(0)),">"),
                        new CompStmt(new PrintStmt(new VarExp("v")), new AssignStmt("v",new ArithExp('-',new VarExp("v"),new ValueExp(new IntValue(1)))))),
                        new PrintStmt(new VarExp("v")))));
        IStmt ex6= new CompStmt(new VarDeclStmt("v",new RefType(new IntType())),new CompStmt(new newV("v",new ValueExp(new IntValue(20))),
                new CompStmt(new VarDeclStmt("a",new RefType(new RefType(new IntType()))),new CompStmt(new newV("a",new VarExp("v")),
                        new CompStmt(new PrintStmt(new VarExp("v")),new PrintStmt(new VarExp("a")))))));
        IStmt ex7=new CompStmt(new VarDeclStmt("v",new RefType(new IntType())),new CompStmt(new newV("v",new ValueExp(new IntValue(20))),
                new CompStmt(new VarDeclStmt("a",new RefType(new RefType(new IntType()))),new CompStmt(new newV("a",new VarExp("v")),
                        new CompStmt(new PrintStmt(new rH(new VarExp("v"))),new PrintStmt(new ArithExp('+',new rH(new rH(new VarExp("a"))),new ValueExp(new IntValue(5)))))))));
        IStmt ex8=new CompStmt(new VarDeclStmt("v",new RefType(new IntType())),new CompStmt(new newV("v",new ValueExp(new IntValue(20))),
                new CompStmt(new PrintStmt(new rH(new VarExp("v"))),new CompStmt(new wH("v",new ValueExp(new IntValue(30))),
                        new PrintStmt(new ArithExp('+',new rH(new VarExp("v")),new ValueExp(new IntValue(5))))))));
        IStmt ex9= new CompStmt(new VarDeclStmt("v",new RefType(new IntType())),new CompStmt(new newV("v", new ValueExp(new IntValue(20))),
                new CompStmt(new VarDeclStmt("a",new RefType(new RefType(new IntType()))),new CompStmt(new newV("a",new VarExp("v")),
                        new CompStmt(new newV("v",new ValueExp(new IntValue(30))),new CompStmt(new PrintStmt(new rH(new rH(new VarExp("a")))),
                                new CompStmt(new VarDeclStmt("i",new RefType(new RefType(new IntType()))),new CompStmt(
                                        new newV("i",new VarExp("v")),new PrintStmt(new rH(new rH(new VarExp("i"))))))))))));
        IStmt ex10=new CompStmt(new VarDeclStmt("v",new IntType()),new CompStmt(new VarDeclStmt("a",new RefType(new IntType())),
                new CompStmt(new AssignStmt("v",new ValueExp(new IntValue(10))),new CompStmt(new newV("a",new ValueExp(new IntValue(22))),
                        new CompStmt(new forkStmt(new CompStmt(new wH("a",new ValueExp(new IntValue(30))),new CompStmt(
                                new AssignStmt("v",new ValueExp(new IntValue(32))),new CompStmt(new PrintStmt(new VarExp("v")),
                                new PrintStmt(new rH(new VarExp("a"))))))),new CompStmt(new PrintStmt(new VarExp("v")),
                                new PrintStmt(new rH(new VarExp("a")))))))));
        IStmt ex11 = new CompStmt( new VarDeclStmt("a",new IntType()),  new CompStmt(new VarDeclStmt("b",new StringType()),
                new CompStmt(new AssignStmt("a", new ArithExp('+',new ValueExp(new IntValue(2)),
                        new ArithExp('*',new ValueExp(new IntValue(3)), new ValueExp(new IntValue(5))))),
                        new CompStmt(new AssignStmt("b",new ArithExp('+',new VarExp("a"), new ValueExp(new IntValue(1)))),
                                new PrintStmt(new VarExp("b"))))));
        IStmt ex12=new CompStmt(new VarDeclStmt("a",new RefType(new IntType())),new CompStmt(new VarDeclStmt("b",new RefType(new IntType())),
                new CompStmt(new VarDeclStmt("v",new IntType()),new CompStmt(new newV("a",new ValueExp(new IntValue(0))),
                        new CompStmt(new newV("b",new ValueExp( new IntValue(0))), new CompStmt(new wH("a",new ValueExp(new IntValue(1))),
                        new CompStmt(new wH("b",new ValueExp(new IntValue(2))),new CompStmt(new CondAsg(new VarExp("v"),new RelExp(
                                new rH(new VarExp("a")),new rH(new VarExp("b")),"<"),new ValueExp(new IntValue(100)),
                                new ValueExp(new IntValue(200))),new CompStmt(new PrintStmt(new VarExp("v")),
                                new CompStmt(new CondAsg(new VarExp("v"),new RelExp(new ArithExp('-',new rH(new VarExp("b")),new ValueExp(new IntValue(2))),
                                        new rH(new VarExp("a")),">"),new ValueExp(new IntValue(100)),new ValueExp(new IntValue(200))),
                                        new PrintStmt(new VarExp("v"))))))))))));
        IStmt ex13=new CompStmt(new VarDeclStmt("v1",new RefType(new IntType())),new CompStmt(new VarDeclStmt("v2",new RefType(new IntType())),
                new CompStmt(new VarDeclStmt("v3",new RefType(new IntType())),new CompStmt(new VarDeclStmt("cnt",new IntType()),
                        new CompStmt(new newV("v1",new ValueExp(new IntValue(2))),new CompStmt(new newV("v2",new ValueExp(new IntValue(3))),
                                new CompStmt(new newV("v3",new ValueExp(new IntValue(4))),new CompStmt(new newLatch("cnt",new rH(new VarExp("v2"))),
                                        new CompStmt(new forkStmt(new CompStmt(new wH("v1",new ArithExp('*',new rH(new VarExp("v1")),
                                                new ValueExp(new IntValue(10)))),new CompStmt(new PrintStmt(new rH(new VarExp("v1"))),
                                                new CompStmt(new countDown("cnt"),new forkStmt(new CompStmt(new wH("v2",new ArithExp('*',new rH(new VarExp("v2")),
                                                        new ValueExp(new IntValue(10)))),new CompStmt(new PrintStmt(new rH(new VarExp("v2"))),
                                                        new CompStmt(new countDown("cnt"),new forkStmt(new CompStmt(new wH("v3",new ArithExp('*',new rH(new VarExp("v3")),
                                                                new ValueExp(new IntValue(10)))),new CompStmt(new PrintStmt(new rH(new VarExp("v3"))),
                                                                new countDown("cnt")))))))))))),new CompStmt(new await("cnt"),
                                                new CompStmt(new PrintStmt(new ValueExp(new IntValue(100))),new CompStmt(new countDown("cnt"),
                                                        new PrintStmt(new ValueExp(new IntValue(100)))))))))))))));


        //Ref int v1; Ref int v2; Ref int v3; int cnt;
        //new(v1,2);new(v2,3);new(v3,4);newLatch(cnt,rH(v2));
        //fork(wh(v1,rh(v1)*10));print(rh(v1));countDown(cnt);
        //  fork(wh(v2,rh(v2)*10));print(rh(v2));countDown(cnt);
        //    fork(wh(v3,rh(v3)*10));print(rh(v3));countDown(cnt))));
        //await(cnt); print(100); countDown(cnt);
        //print(100)
        try {
            PrgState prg1 = new PrgState(ex1);
            PrgState prg2 = new PrgState(ex2);
            PrgState prg3 = new PrgState(ex3);
            PrgState prg4 = new PrgState(ex4);
            PrgState prg5 = new PrgState(ex5);
            PrgState prg6 = new PrgState(ex6);
            PrgState prg7 = new PrgState(ex7);
            PrgState prg8 = new PrgState(ex8);
            PrgState prg9 = new PrgState(ex9);
            PrgState prg10 = new PrgState(ex10);
            PrgState prg12 = new PrgState(ex12);
            PrgState prg13 = new PrgState(ex13);
            //PrgState prg11 = new PrgState(ex11);

            repository1.add(prg1);
            repository2.add(prg2);
            repository3.add(prg3);
            repository4.add(prg4);
            repository5.add(prg5);
            repository6.add(prg6);
            repository7.add(prg7);
            repository8.add(prg8);
            repository9.add(prg9);
            repository10.add(prg10);
            repository12.add(prg12);
            repository13.add(prg13);
            //repository11.add(prg11);

            Controller controller1 = new Controller(repository1);
            Controller controller2 = new Controller(repository2);
            Controller controller3 = new Controller(repository3);
            Controller controller4 = new Controller(repository4);
            Controller controller5 = new Controller(repository5);
            Controller controller6 = new Controller(repository6);
            Controller controller7 = new Controller(repository7);
            Controller controller8 = new Controller(repository8);
            Controller controller9 = new Controller(repository9);
            Controller controller10 = new Controller(repository10);
            Controller controller12 = new Controller(repository12);
            Controller controller13 = new Controller(repository13);
            //Controller controller11 = new Controller(repository11);

            TextMenu menu = new TextMenu();
            menu.addCommand(new ExitCommand("0", "exit"));
            menu.addCommand(new RunExample("1", ex1.toString(), controller1));
            menu.addCommand(new RunExample("2", ex2.toString(), controller2));
            menu.addCommand(new RunExample("3", ex3.toString(), controller3));
            menu.addCommand(new RunExample("4", ex4.toString(), controller4));
            menu.addCommand(new RunExample("5", ex5.toString(), controller5));
            menu.addCommand(new RunExample("6", ex6.toString(), controller6));
            menu.addCommand(new RunExample("7", ex7.toString(), controller7));
            menu.addCommand(new RunExample("8", ex8.toString(), controller8));
            menu.addCommand(new RunExample("9", ex9.toString(), controller9));
            menu.addCommand(new RunExample("10", ex10.toString(), controller10));
            menu.addCommand(new RunExample("12", ex12.toString(), controller12));
            menu.addCommand(new RunExample("13", ex13.toString(), controller13));
            //menu.addCommand(new RunExample("11", ex10.toString(), controller11));

            menu.show();
        } catch (InterruptedException | MyException e) {
            System.out.println(e.getMessage());
        }

    }
}
