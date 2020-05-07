import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from random import randint


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
    for i in range((len(x) * 80) // 100):
        number = randint(0, len(x) - 1)
        while x[number] in xtrain:
            number = randint(0, len(x) - 1)
        xtrain.append(x[number])
        x.pop(number)
        ytrain.append(y[number])
        y.pop(number)

    return xtrain,x,ytrain,y

class NeuralNetwork:

    def __init__(self, xtrain, ytrain):
        self.input = xtrain
        self.y = ytrain
        self.hidden = None
        self.output = np.zeros(self.y.shape)
        print(self.input.shape)
        self.weights1 = np.random.rand(self.input.shape[1],2)
        self.weights2 = np.random.rand(2, self.input.shape[1])

        self.loss = []

    def feed_forward(self):
        self.hidden = np.dot(self.input, self.weights1)
        self.output = np.dot(self.hidden, self.weights2)

    def back_propagation(self, l_rate):
        deltaweights2 = np.dot(self.hidden.T, self.y - self.output)
        deltaweights1 = np.dot(self.input.T, (np.dot(self.y - self.output, self.weights2.T)))

        self.weights1 += l_rate * deltaweights1
        self.weights2 += l_rate * deltaweights2
        self.loss.append(sum(self.y - self.output))




def runANN():

    x_train, x_test, y_train, y_test = pickTrainingTest()
    train = len(x_train)
    print(train)


    X = np.array([np.array(el) for el in x_train])
    print(X.shape,"*")
    Y = np.array([[np.array(el)] for el in y_train])
    network = NeuralNetwork(X, Y, train)

    network.loss = []
    iterations = []
    for i in range(1000):
        network.feed_forward()
        network.back_propagation(0.00000001)
        iterations.append(i)

    # w = network.weights2[-5:]
    w=network.weights2[-1]
    print(w)
    sumD, maxD, maxY = 0, 0, 0
    maxX=[]
    for x, expected in zip(x_test, y_test):
        predict = w[0] * x[0] + w[1] * x[1] + w[2] * x[2] + w[3] * x[3] + w[4] * x[4]
        d = abs(expected - predict)
        sumD += d
        if d>maxD:
            maxD=d
            maxY=expected
            maxX=x
    avg = sumD / len(x_test)
    print("Average difference: ", avg)
    print("Biggest difference: ",maxD," for values:")
    print("x=",maxX," y=",maxY)

    mpl.pyplot.plot(iterations, network.loss, label='loss value vs iteration')
    mpl.pyplot.xlabel('Iterations')
    mpl.pyplot.ylabel('Error')
    mpl.pyplot.legend()
    mpl.pyplot.show()

runANN()