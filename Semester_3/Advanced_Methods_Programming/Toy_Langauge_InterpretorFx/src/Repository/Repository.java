package Repository;

import Exceptions.MyException;
import Model.PrgState;

import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Repository implements IRepository {
    private List<PrgState> list;
    private String logFilePath;

    public Repository() {
        list = new ArrayList<>();
        Scanner input=new Scanner(System.in);
        System.out.println("Give path to log text file:");
        logFilePath=input.nextLine();
    }

    public Repository(String path){
        list = new ArrayList<>();
        logFilePath=path;
    }

    @Override
    public PrgState getPrgById(int id) {
        for(PrgState p: list){
            if (p.getId()==id)return p;
        }
        return null;
    }

    public void logPrgStateExec(PrgState prg) throws MyException{
        PrintWriter logFile;
        try {
            logFile = new PrintWriter(new BufferedWriter(new FileWriter(logFilePath, true)));
            logFile.printf(prg.toString());
            logFile.close();
        }
        catch (IOException e){
            System.out.println(e.getMessage());
        }
    }

    public void setPrgList(List<PrgState> list) {
        this.list = list;
    }

    @Override
    public List<PrgState> getPrgList() {
        return list;
    }

    public void add(PrgState state){ list.add(state);}

}
