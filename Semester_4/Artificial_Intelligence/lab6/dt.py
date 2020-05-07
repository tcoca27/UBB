from node import Node
from random import randint
from copy import deepcopy
from math import log2

class Tree:
    def __init__(self,training):
        self._training=training
        self._root=Node()

    def setRoot(self,root):
        self._root=root

    def getTraining(self):
        return self._training

    def __str__(self):
        return str(self._root)

    def generate(self,D,A,value=0):
        N=Node()
        N.setValue(value)
        classDict=self.classCounter(D)
        key=list(classDict.keys())[2]
        if classDict[key]==len(D) or len(A)==0:
            N.setRoot(key)
            return N
        else:
            separation_attribute=self.AttributeSelectionInfoGain(D,A)
            N.setRoot(separation_attribute)
            for i in range(1,6):
                newD=[]
                for val in D:
                    if val[separation_attribute]==i:
                        newD.append(val)
                if len(newD)==0:
                    N.addChild(Node(key))
                else:
                    incA=deepcopy(A)
                    incA.remove(separation_attribute)
                    N.addChild(self.generate(newD,incA,i))
            return N

    def classCounter(self, D):
        dc={'L':0,'R':0,'B':0}
        for line in D:
            dc.update({line[0]:dc.get(line[0])+1})
        dc={k: v for k, v in sorted(dc.items(), key=lambda item: item[1])}
        return dc

    def AttributeSelectionGiniIndex(self,D,A):
        if len(A)==1:
            return A[0]
        values={}
        for i in A:
            values.update({i:randint(2,4)})
        for key in values.keys():
            l,b,r=0,0,0
            lsmall,rsmall,bsmall=0,0,0
            for val in D:
                if(val[key]>=values.get(key)):
                    if val[0]=='L':
                        l+=1
                    if val[0]=='R':
                        r+=1
                    if val[0]=='B':
                        b+=1
                else:
                    if val[0]=='L':
                        lsmall+=1
                    if val[0]=='R':
                        rsmall+=1
                    if val[0]=='B':
                        bsmall+=1
            totalBig=l+r+b
            totalSmall=lsmall+rsmall+bsmall
            giniBig=1-(pow(l/totalBig,2)+pow(b/totalBig,2)+pow(r/totalBig,2))
            giniSmall=1-(pow(lsmall/totalSmall,2)+pow(bsmall/totalSmall,2)+pow(rsmall/totalSmall,2))
            gini=(totalBig/(totalSmall+totalBig))*giniBig+(totalSmall/(totalSmall+totalBig))*giniSmall
            values.update({key:gini})
        values={k: v for k, v in sorted(values.items(), key=lambda item: item[1])}
        return list(values.keys())[0]

    def AttributeSelectionInfoGain(self,D,A):
        if len(A)==1:
            return A[0]
        l,b,r=0,0,0
        for val in D:
            if val[0] == 'L':
                l += 1
            if val[0] == 'R':
                r += 1
            if val[0] == 'B':
                b += 1
        total=l+b+r
        E=0
        if total > 0:
            if l > 0:
                E = -(l / total) * log2(l / total)
            if r > 0:
                E -= r / total * log2(r / total)
            if b > 0:
                E -= b / total * log2(b / total)

        maxGain=0
        maxAttr=None
        for i in range(len(A)):
            Ei=E
            l, b, r = 0, 0, 0
            for j in range(1,6):
                for val in D:
                    if val[A[i]]==j:
                        if val[0] == 'L':
                            l += 1
                        if val[0] == 'R':
                            r += 1
                        if val[0] == 'B':
                            b += 1
                total=l+b+r
                if total>0:
                    if l>0:
                        Ei-=(l/total)*log2(l/total)
                    if r>0:
                        Ei-=r/total*log2(r/total)
                    if b>0:
                        Ei-=b/total*log2(b/total)
            if Ei>maxGain:
                maxGain=Ei
                maxAttr=A[i]
        return maxAttr

    def clasify(self,value):
        queue=[self._root]
        currentN=None
        while len(queue):
            currentN=queue.pop()
            children=currentN.getChildren()
            for i in range(len(children)):
                if children[i].getValue()==value[currentN.getRoot()]:
                    queue.append(children[i])
        return currentN.getRoot()==value[0]