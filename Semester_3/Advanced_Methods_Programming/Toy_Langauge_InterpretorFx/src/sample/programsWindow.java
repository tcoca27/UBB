package sample;

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
import Repository.IRepository;
import Repository.Repository;
import javafx.collections.FXCollections;
import javafx.fxml.FXML;
import javafx.fxml.Initializable;
import javafx.scene.control.Button;
import javafx.scene.control.ListView;

import java.net.URL;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.ResourceBundle;
import java.util.concurrent.Executor;
import java.util.stream.Collectors;

public class programsWindow implements Initializable {
    private List<IStmt> prgStms;
    private PrgViewCtrl prgViewCtrl;

    @FXML private ListView<String> PrgList;
    @FXML private Button ExecuteButton;
    @FXML private Button ExitButton;

    public void setPrgViewCtrl(PrgViewCtrl prgViewCtrl){
        this.prgViewCtrl=prgViewCtrl;
    }

    private void buildPrgs(){
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
        prgStms= new ArrayList<>(Arrays.asList(ex1,ex2,ex3,ex4,ex5,ex6,ex7,ex8,ex9,ex10,ex11,ex12,ex13));
    }

    private List<String> PrgStateToString(){
        return prgStms.stream().map(IStmt::toString).collect(Collectors.toList());
    }

    @Override
    public void initialize(URL url, ResourceBundle resourceBundle) {
        buildPrgs();
        PrgList.setItems(FXCollections.observableArrayList(PrgStateToString()));
        ExecuteButton.setOnAction(actionEvent -> {
            int index=PrgList.getSelectionModel().getSelectedIndex();
            if(index<0)
                return;
            try {
                PrgState initial= new PrgState(prgStms.get(index));
                IRepository repo=new Repository("log"+index+".txt");
                repo.add(initial);
                Controller ctrl=new Controller(repo);
                prgViewCtrl.setController(ctrl);
            } catch (MyException e) {
                e.printStackTrace();
            }
        });
        ExitButton.setOnAction(actionEvent -> System.exit(0));
    }
}
