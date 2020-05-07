from controller import Controller
from dt import Tree

class Problem:
    def __init__(self,path):
        self._path=path

    def readData(self):
        file=open(self._path,"r")
        lines=file.readlines()
        data=[]
        for line in lines:
            atrs=line.split(',')
            data.append([atrs[0],int(atrs[1]),int(atrs[2]),int(atrs[3]),int(atrs[4])])
        return data

    def start(self):
        ctrl= Controller(self.readData())
        tnt=ctrl.pickTrainingandTest(80)
        t=Tree(tnt[0])
        t.setRoot(t.generate(t.getTraining(),[1,2,3,4]))
        true=0
        for i in range(len(tnt[1])):
            if t.clasify(tnt[1][i])==True:
                true+=1
        accuracy=(true*100)/len(tnt[1])
        print("Accuracy="+str(accuracy))

p= Problem("balance-scale.data")
p.start()
