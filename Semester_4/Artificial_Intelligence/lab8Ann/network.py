from copy import deepcopy
from firstLayer import FirstLayer
from layer import Layer
import matplotlib as mpl
from random import randint


class Network:
    def __init__(self,inputs,outputs):
        self.hidden=Layer(5,1)
        self.inputLayer=Layer(5,1)
        self.outLayer=Layer(5,1)
        self.inputs=inputs
        self.outputs=outputs


    def feedForward(self,inputs):
        self.signal = deepcopy(inputs)
        self.signal = self.inputLayer.forward(self.signal)
        self.signal = self.hidden.forward(self.signal)
        self.signal = self.outLayer.forward(self.signal)
        return self.signal

    def derivative(self,i):
        return self.inputs[i]*(self.feedForward([self.inputs[i]])-self.outputs[i])

    def backPropag(self, loss, learnRate):
        err = loss[:]
        delta = []
        newConfig=Network(self.inputs,self.outputs)
        # last layer
        for i in range(len(self.inputs)):
            delta.append(sum([j for j in self.inputs[i]]*self.computeLoss(self.inputs[i],self.outputs[i])))
            for r in range(5):
                newConfig.outLayer.neurons[0].weights[r] = self.outLayer.neurons[0].weights[r] + learnRate * delta[i]* self.hidden.neurons[0].output

        currentDelta = []
        for i in range(len(self.inputs)):
            for r in range(5):
                currentDelta.append(self.derivate * sum(
                    [self.hidden.neurons[0].weights[r] * delta[i]))

            delta = currentDelta[:]
            for i in range(self.structure[currentLayer]):
                for r in range(self.structure[currentLayer - 1]):
                    newConfig.layers[currentLayer].neurons[i].weights[r] = self.layers[currentLayer].neurons[i].weights[r] + learnRate * delta[i] * \
                                                                           self.layers[currentLayer - 1].neurons[r].output
        self.layers = deepcopy(newConfig.layers)

    def computeLoss(self, inputs, expectedOut):
        out = self.feedForward(inputs)
        return expectedOut - out[0]

    def __str__(self):
        s = ''
        for i in range(self.noLayers):
            s += ' l ' + str(i) + ' :' + str(self.layers[i])
        return s


def loadDB(path):
    x=[]
    y=[]
    file=open(path,'r')
    lines=file.readlines()
    for line in lines:
        xline=[]
        attrs=line.split(" ")
        if len(attrs)==6:
            xline.append(float(attrs[0]))
            xline.append(float(attrs[1]))
            xline.append(float(attrs[2]))
            xline.append(float(attrs[3]))
            xline.append(float(attrs[4]))
            y.append(float(attrs[5]))
            x.append(xline)
    return x,y

def pickTrainingTest():
    x,y=loadDB("bdate2.txt")
    xtrain,ytrain=[],[]
    for i in range((len(x) * 100) // 100):
        number = randint(0, len(x) - 1)
        while x[number] in xtrain:
            number = randint(0, len(x) - 1)
        xtrain.append(x[number])
        x.pop(number)
        ytrain.append(y[number])
        y.pop(number)
    return xtrain,x,ytrain,y

def test1():
    nn = Network([5, 1, 1])
    u,utest,t,ttrain=pickTrainingTest()
    iterations = []
    errors=[]
    for i in range(1500):
        iterations.append(i)
        e = []
        for j in range(len(u)):
            e.append(nn.computeLoss(u[j], t[j])[0])
            nn.backPropag(nn.computeLoss(u[j], t[j]), 0.00001)
        errors.append(sum([x / len(e) for x in e]))
    for j in range(len(u)):
        nn.feedForward(u[j])
        print(u[j], t[j], nn.feedForward(u[j]))
    print(str(nn))
    mpl.pyplot.plot(iterations, errors, label='loss value vs iteration')
    mpl.pyplot.xlabel('Iterations')
    mpl.pyplot.ylabel('loss function')
    mpl.pyplot.legend()
    mpl.pyplot.show()
    
test1()
