package View;

import Controller.Controller;
import Exceptions.MyException;

public class RunExample extends Command {
    private Controller ctr;

    public RunExample(String key, String desc,Controller ctr){
        super(key, desc);
        this.ctr=ctr;
    }

    @Override
    public void execute() throws InterruptedException{
        try{
            ctr.allStep(0);
        }
        catch (MyException e)  { System.out.println(e.getMessage());}
    }
}
