package sample;

import Collection.Dictionary.MyIDictionary;
import Collection.Heap.MyIHeap;
import Collection.LTable.MyILTable;
import Collection.MyIList.MyIList;
import Collection.Stack.MyIStack;
import Controller.Controller;
import Model.PrgState;
import Model.Stament.IStmt;
import Model.Values.StringValue;
import Model.Values.Value;
import javafx.beans.property.SimpleIntegerProperty;
import javafx.beans.property.SimpleObjectProperty;
import javafx.beans.property.SimpleStringProperty;
import javafx.collections.FXCollections;
import javafx.fxml.FXML;
import javafx.fxml.Initializable;
import javafx.scene.control.*;

import java.io.BufferedReader;
import java.io.File;
import java.net.URL;
import java.util.*;
import java.util.stream.Collectors;

public class PrgViewCtrl implements Initializable {
    private Controller controller;
    @FXML private TableView<Map.Entry<Integer,Value>> HeapTableView;
    @FXML private TableColumn<Map.Entry<Integer,Value>,Integer> AddressColumn;
    @FXML private TableColumn<Map.Entry<Integer,Value>,Value> ValueColumn;
    @FXML private TableView<Map.Entry<String,Value>> SymTblView;
    @FXML private TableColumn<Map.Entry<String,Value>,String> VarNameColumn;
    @FXML private TableColumn<Map.Entry<String,Value>,Value> ValueSymColumn;
    @FXML private ListView<String> OutView;
    @FXML private ListView<Value> FileTableView;
    @FXML private ListView<Integer> PrgStateIDView;
    @FXML private ListView<String> ExeStackView;
    @FXML private TextField NrPrgSt;
    @FXML private Button RunButton;
    @FXML private Button ExitButton;
    @FXML private TableView<Map.Entry<Integer,Integer>> latchTableView;
    @FXML private TableColumn<Map.Entry<Integer,Integer>,Integer> locationColumn;
    @FXML private TableColumn<Map.Entry<Integer,Integer>,Integer> valueColumn;
    private Main main;

    public void setController(Controller ctrl){
        controller=ctrl;
        populatePrgIDView();
    }

    public void setMain(Main main) {
        this.main = main;
    }

    public void populatePrgIDView(){
        List<PrgState> prgStates=controller.getRepository().getPrgList();
        PrgStateIDView.setItems(FXCollections.observableList(getPID(prgStates)));
        NrPrgSt.setText(Integer.toString(prgStates.size()));
    }

    private List<Integer> getPID(List<PrgState> prgStates){
        return prgStates.stream().map(PrgState::getId).collect(Collectors.toList());
    }

    @Override
    public void initialize(URL url, ResourceBundle resourceBundle) {
        AddressColumn.setCellValueFactory(p-> new SimpleIntegerProperty(p.getValue().getKey()).asObject());
        ValueColumn.setCellValueFactory(p-> new SimpleObjectProperty(p.getValue().getValue()));

        VarNameColumn.setCellValueFactory(p->new SimpleStringProperty(p.getValue().getKey()+""));
        ValueSymColumn.setCellValueFactory(p-> new SimpleObjectProperty(p.getValue().getValue()));

        locationColumn.setCellValueFactory(p-> new SimpleObjectProperty(p.getValue().getValue()));
        valueColumn.setCellValueFactory(p-> new SimpleObjectProperty(p.getValue().getValue()));

        PrgStateIDView.setOnMouseClicked(mouseEvent -> { changePrg(getCurrentPrg());});

        RunButton.setOnAction(actionEvent -> {executeOneStep();});

        ExitButton.setOnAction(actionEvent -> {System.exit(0);});
    }

    private void executeOneStep(){
        if(controller==null){
            Alert alert= new Alert(Alert.AlertType.ERROR,"No program to be executed", ButtonType.OK);
            alert.showAndWait();
            return;
        }

        boolean prgState=getCurrentPrg().getStk().isEmpty();
        if(prgState){
            Alert alert= new Alert(Alert.AlertType.ERROR,"Program is done", ButtonType.OK);
            alert.showAndWait();
            return;
        }

        controller.executeOneStep();

        changePrg(getCurrentPrg());
        populatePrgIDView();
    }

    private void changePrg(PrgState current){
        if(current==null)return;
        populateExeStack(current);
        populateSymTbl(current);
        populateOut(current);
        populateFileTbl(current);
        populateHeap(current);
        populateLatch(current);
    }

    private PrgState getCurrentPrg(){
        if(PrgStateIDView.getSelectionModel().getSelectedIndex()==-1)
            return null;
        int current=PrgStateIDView.getSelectionModel().getSelectedItem();
        return controller.getRepository().getPrgById(current);
    }

    private void populateOut(PrgState current){
        MyIList<Value> out=current.getOut();
        List<Value> outl = new ArrayList<>(out.getAll());
        OutView.setItems(FXCollections.observableList(outl.stream().map(Value::toString).collect(Collectors.toList())));
        OutView.refresh();
    }

    private void populateExeStack(PrgState current){
        MyIStack<IStmt> exeStk=current.getStk();
        List<String> exeList=new ArrayList<>();
        for(IStmt s:exeStk.getAll())exeList.add(s.toString());
        ExeStackView.setItems(FXCollections.observableList(exeList));
        ExeStackView.refresh();
    }

    private void populateSymTbl(PrgState current){
        MyIDictionary<String,Value> symTbl=current.getSymTable();
        List<Map.Entry<String,Value>> entries=new ArrayList<>();
        for(Map.Entry<String,Value> entry: symTbl.getDict()){
            entries.add(entry);
        }
        SymTblView.setItems(FXCollections.observableList(entries));
        SymTblView.refresh();
    }

    private void populateLatch(PrgState current){
        MyILTable<Integer,Integer> symTbl=current.getLatchTable();
        List<Map.Entry<Integer,Integer>> entries=new ArrayList<>();
        for(Map.Entry<Integer,Integer> entry: symTbl.getDict()){
            entries.add(entry);
        }
        latchTableView.setItems(FXCollections.observableList(entries));
        latchTableView.refresh();
    }

    private void populateFileTbl(PrgState current){
        MyIDictionary<StringValue, BufferedReader> ft=current.getFileTable();
        List<Value> newft=new ArrayList<>();
        for (Value val:ft.getKeys())
            newft.add(val);
        FileTableView.setItems(FXCollections.observableList(newft));
        FileTableView.refresh();
    }

    private void populateHeap(PrgState current){
        MyIHeap<Integer,Value> heap=current.getHeap();

        List<Map.Entry<Integer,Value>> entries=new ArrayList<>();
        for(Map.Entry<Integer,Value> entry: heap.getHeap())
            entries.add(entry);

        HeapTableView.setItems(FXCollections.observableList(entries));
        HeapTableView.refresh();
    }
}
