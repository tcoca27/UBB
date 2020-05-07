# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 23:37:00 2020

@author: tudor
"""

from random import random,choice
from copy import deepcopy

class Ant:
    def __init__(self,n):
        self._n=n
        self._solution=[[0 for i in range(n) ] for i in range(2*n)]
        
    def getSolution(self):
        return self._solution
    
    def buildMatrix(self,m):
        matrix=[[[0,0] for i in range(self._n)] for j in range(self._n)]
        for i in range(2*self._n):
            for j in range(self._n):
                matrix[i%self._n][j][i//self._n]=m[i][j]
        return matrix
    
    def prettyPrint(self,matrix):
        s=""
        for i in matrix:
            s+="\n"
            for j in i:
                s+=str(j)
                s+=' '
        return s
    
    def fitness(self,sol):
        matrix=self.buildMatrix(sol)
        numbers=[]
        pairs=[]
        mistakes=0
        for j in range(self._n):
            numbers=[]
            for k in range(2):
                numbers=[]
                for i in range (self._n):
                    if matrix[i][j][k] in numbers:
                        mistakes+=1
                    numbers.append(matrix[i][j][k])
        for col in matrix:
            for pair in col:
                if pair in pairs:
                    mistakes+=1
                pairs.append(pair)
        return mistakes
    
    def nextMoveFitness(self,a):
        sol=deepcopy(self._solution)
        end=0
        for perm in sol:
            for i in range(len(perm)):
                if perm[i]==0:
                    perm[i]=a
                    end+=1
                    break
            if end>0:
                break
        return abs(self.fitness(self._solution)-self.fitness(sol))
        
    
    def nextMoves(self,i):
        possibleMoves=[]
        for j in range(1,self._n+1):
            possibleMoves.append(j)
        for value in self._solution[i]:
            if value in possibleMoves:
                possibleMoves.remove(value)
        return possibleMoves
    
    def indexOfNextMove(self):
        for i in range(2*self._n):
            for j in range(self._n):
                if self._solution[i][j]==0:
                    return i,j
    
    def addMove(self,beta,trace,alpha,q0):
        indexi,indexj=self.indexOfNextMove()
        nextMoves=self.nextMoves(indexi)
        p=[]
        for move in nextMoves:
            p.append([move,self.nextMoveFitness(move)]) #move and distance
        for move in p:
            move[1]=(move[1]**beta)*(trace[indexi*3+indexj][move[0]-1]*alpha)
        if random()<q0:
            p=max(p,key=lambda a:a[1])
            self._solution[indexi][indexj]=p[0]
        else:
            s=0
            for move in p:
                s+=move[1]
            if s==0:
                self._solution[indexi][indexj]=choice(nextMoves)
                return
            for move in p:
                move[1]=move[1]/s
            for i in range(len(p)):
                s=0
                for j in range(i+1):
                    s+=p[j][1]
                p[i][1]=s
            r=random()
            i=0
            while(r>p[i][1]):
                i+=1
            self._solution[indexi][indexj]=p[i][0]
        
#ant=Ant(3)
#trace=[[1 for i in range(3) ] for i in range(2*3*3)]


#ant.addMove(0.9,trace,1.9,0.5)
#ant.addMove(0.9,trace,1.9,0.5)
#ant.addMove(0.9,trace,1.9,0.5)
#ant.addMove(0.9,trace,1.9,0.5)
#ant.addMove(0.9,trace,1.9,0.5)
#ant.addMove(0.9,trace,1.9,0.5)
#ant.addMove(0.9,trace,1.9,0.5)
#ant.addMove(0.9,trace,1.9,0.5)
#ant.addMove(0.9,trace,1.9,0.5)
#ant.addMove(0.9,trace,1.9,0.5)
#ant.addMove(0.9,trace,1.9,0.5)
#ant.addMove(0.9,trace,1.9,0.5)
#ant.addMove(0.9,trace,1.9,0.5)
#ant.addMove(0.9,trace,1.9,0.5)
#ant.addMove(0.9,trace,1.9,0.5)
#ant.addMove(0.9,trace,1.9,0.5)
#ant.addMove(0.9,trace,1.9,0.5)
#ant.addMove(0.9,trace,1.9,0.5)

#print(ant.prettyPrint(ant.buildMatrix(ant.getSolution())))