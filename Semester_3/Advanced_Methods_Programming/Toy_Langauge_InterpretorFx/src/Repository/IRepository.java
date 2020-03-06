package Repository;

import Exceptions.MyException;
import Model.PrgState;
import Model.Stament.IStmt;

import java.util.List;

public interface IRepository {
    void add(PrgState prg);
    void logPrgStateExec(PrgState prg) throws MyException;
    List<PrgState> getPrgList();
    PrgState getPrgById(int id);
    void setPrgList(List<PrgState> l) ;
}
