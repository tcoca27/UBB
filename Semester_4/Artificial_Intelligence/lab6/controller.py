from dt import Tree
from random import randint

class Controller:
    def __init__(self,database):
        self._data=database

    def pickTrainingandTest(self,percentage):
        training=[]
        test=[]
        for i in range( (len(self._data)*percentage)//100 ):
            number=randint(0,len(self._data)-1)
            while self._data[number] in training:
                number = randint(0, len(self._data)-1)
            training.append(self._data[number])
        for val in self._data:
            if val not in training:
                test.append(val)
        return training,test
