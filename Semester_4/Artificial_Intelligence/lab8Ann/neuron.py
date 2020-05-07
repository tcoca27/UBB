from random import random

class Neuron:
    def __init__(self,nrinputs):
        self.nrinputs=nrinputs
        self.weights=[random() for i in range(nrinputs)]
        self.output=0

    def activate(self,inputs):
        s=sum([x*y for x,y in zip(inputs,self.weights)])
        self.output=s

    def setWeights(self,new):
        self.weights=new

    def getWeights(self):
        return self.weights

    def __str__(self):
        return str(self.weights)
