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
    for i in range((len(x) * 85) // 100):
        number = randint(0, len(x) - 1)
        while x[number] in xtrain:
            number = randint(0, len(x) - 1)
        xtrain.append(x[number])
        x.pop(number)
        ytrain.append(y[number])
        y.pop(number)
    return xtrain,x,ytrain,y


def gradientDescend(x,y,lr,epochs):
    c=0
    m=[0.0,0.0,0.0,0.0,0.0]
    stepSize=[1,1,1,1,1]
    stepSizeC=1
    minstepSize=[10,10,10,10,10]
    minstepSizeC=10
    while epochs>0 and (abs(minstepSize[0])>0.001 or abs(minstepSize[1])>0.001 or abs(minstepSize[2])>0.001 or abs(minstepSize[3])>0.001 or abs(minstepSize[4])>0.001 or abs(minstepSizeC)>0.001):
        sumResidual=0.0
        sumDerivativeC=0.0
        sumDerivativeM= [0.0, 0.0, 0.0, 0.0, 0.0]
        for i in range(len(x)):
            residual=y[i]-(c+m[0]*x[i][0]+m[1]*x[i][1]+m[2]*x[i][2]+m[3]*x[i][3]+m[4]*x[i][4])
            sumResidual+=residual
            sumDerivativeC+=-2*residual
            for j in range(len(sumDerivativeM)):
                sumDerivativeM[j]+=-2*x[i][j]*residual
        stepSizeC=sumDerivativeC*lr
        for i in range(len(stepSize)):
            stepSize[i]=sumDerivativeM[i]*lr
        if minstepSizeC>abs(stepSizeC):
            c-=stepSizeC
            minstepSizeC=abs(stepSizeC)
        for i in range(len(minstepSize)):
            if minstepSize[i]>abs(stepSize[i]):
                m[i]-=stepSize[i]
                minstepSize[i]=abs(stepSize[i])
        epochs-=1
    return c,m


def testDiff2(lr,epochs):
    xtrain,xtest,ytrain,ytest=pickTrainingTest()
    c,m=gradientDescend(xtrain,ytrain,lr,epochs)
    sumDifferences=0
    maxDiff=0
    for i in range(len(xtest)):
        prediction=m[0]*xtest[i][0]+m[1]*xtest[i][1]+m[2]*xtest[i][2]+m[3]*xtest[i][3]+m[4]*xtest[i][4]+c
        diff=abs(ytest[i]-prediction)
        if maxDiff<diff:
            maxDiff=diff
            maxX=xtest[i]
            maxY=ytest[i]
        sumDifferences+=diff
    return sumDifferences/len(xtest), maxDiff,maxX,maxY

result=testDiff2(0.000001,1000)
print("Average difference for values: ",result[0])
print("Biggest difference is: ",result[1])
print("happening for attributes: ",result[2],"=",result[3])