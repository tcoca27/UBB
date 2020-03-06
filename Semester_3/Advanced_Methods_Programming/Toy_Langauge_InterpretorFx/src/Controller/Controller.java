package Controller;

import Collection.Stack.MyIStack;
import Exceptions.MyException;
import Model.PrgState;
import Model.Stament.IStmt;
import Model.Types.RefType;
import Model.Values.RefValue;
import Model.Values.Value;
import Repository.IRepository;

import java.io.IOException;
import java.util.Collection;
import java.util.List;
import java.util.Map;
import java.util.concurrent.Callable;
import java.util.concurrent.ExecutionException;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class Controller {
     private IRepository repository;
     private ExecutorService executor;

     public Controller(IRepository repo){
         repository=repo;
     }

    public void setRepository(IRepository repository) {
        this.repository = repository;
    }

    public IRepository getRepository() {
        return repository;
    }

    Map<Integer, Value> unsafeGarbageCollector(List<Integer> symTableAddr, Map<Integer,Value> heap){
         return heap.entrySet().stream()
                 .filter(e->symTableAddr.contains(e.getKey()))
                         .collect(Collectors.toMap(Map.Entry::getKey, Map.Entry::getValue));}

    List<Integer> getAddrFromSymTable(Collection<Value> symTableValues,Collection<Value>heap){
         return Stream.concat(heap.stream().filter(v->v instanceof RefValue)
         .map(v-> {RefValue v1=(RefValue)v;return v1.getAddress();}),
                 symTableValues.stream().filter(v->v instanceof RefValue)
         .map(v->{RefValue v1= (RefValue)v;return v1.getAddress();})).distinct().collect(Collectors.toList());
     }

    List<PrgState> removeCompletedPrg(List<PrgState> inPrgList){
         return inPrgList.stream().filter(p->p.isNotCompleted()).collect(Collectors.toList());
    }

    public void executeOneStep() {
        executor = Executors.newFixedThreadPool(8);
        removeCompletedPrg(repository.getPrgList());
        List<PrgState> programStates = repository.getPrgList();
        if(programStates.size() > 0)
        {
            try {
                oneStepForAllPrg(repository.getPrgList());
            } catch (InterruptedException | MyException e) {
                System.out.println();
            }
            programStates.forEach(e -> {
                try {
                    repository.logPrgStateExec(e);
                } catch (MyException e1) {
                    System.out.println();
                }
            });
            removeCompletedPrg(repository.getPrgList());
            executor.shutdownNow();
        }
    }

    private void oneStepForAllPrg(List<PrgState> prgList) throws MyException, InterruptedException {
        prgList.forEach(prg -> {
            try {
                repository.logPrgStateExec(prg);
            } catch (MyException e) {
                e.printStackTrace();
            }
        });
        List<Callable<PrgState>> callList=prgList.stream()
                 .map((PrgState p)->(Callable<PrgState>)(()->{return p.oneStep();}))
                 .collect(Collectors.toList());
         List<PrgState> newPrgList=executor.invokeAll(callList).stream()
                 .map(future->{try{return future.get();}
                 catch (InterruptedException | ExecutionException e){System.out.println(e.getMessage());}return null;})
                 .filter(p->p!=null).collect(Collectors.toList());
         prgList.addAll(newPrgList);
        prgList.forEach(prg -> {
            try {
                repository.logPrgStateExec(prg);
            } catch (MyException e) {
                e.printStackTrace();
            }
        });
        repository.setPrgList(prgList);
     }

    public void allStep(int printAfterOne) throws MyException,InterruptedException {
        executor= Executors.newFixedThreadPool(2);
        List<PrgState> prgList=removeCompletedPrg(repository.getPrgList());
        while(prgList.size()>0){
            for(PrgState prg: prgList)
                prg.getHeap().setContent(unsafeGarbageCollector( getAddrFromSymTable(prg.getSymTable().getContent().values()
                        ,prg.getHeap().getContent().values()), prg.getHeap().getContent()));
            oneStepForAllPrg(prgList);
            prgList=removeCompletedPrg(repository.getPrgList());
        }
        executor.shutdownNow();
        repository.setPrgList(prgList);
    }
}
