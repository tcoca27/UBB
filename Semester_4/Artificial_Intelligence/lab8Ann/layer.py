from neuron import Neuron
from random import random

class Layer:
    def __init__(self,nrInputs,nrNeurons):
        self.nrNeurons=nrNeurons
        self.neurons=[Neuron(nrInputs) for i in range(nrNeurons)]
        r=random()
        [x.setWeights([random()]*nrInputs) for x in self.neurons]

    def forward(self, inputs):
        for x in self.neurons:
            x.activate(inputs)
        return([x.output for x in self.neurons])

    def getNeurons(self):
        return self.nrNeurons
        
    def __str__(self):
        s = ''
        for i in range(self.nrNeurons):
            s += ' n '+str(i)+' '+str(self.neurons[i])+'\n'
        return s