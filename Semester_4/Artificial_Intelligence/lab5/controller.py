# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 01:25:21 2020

@author: tudor
"""

from ant import Ant
from copy import deepcopy

class Controller:
    def __init__(self,size,n,alpha,beta,q0,degradation):
        self._colony=[]
        self._size=size
        self._alpha=alpha
        self._beta=beta
        self._q0=q0
        self._rho=degradation
        self._trace=[[1 for i in range(n) ] for i in range(2*n*n)]
        self._n=n

        
    def iteration(self):
        self._colony=[Ant(self._n) for i in range(self._size)]
        for i in range(2*self._n*self._n):
            for ant in self._colony:
                ant.addMove(self._beta, self._trace, self._alpha, self._q0)
        pheromoneQ=[1.0 / self._colony[i].fitness(self._colony[i].getSolution()) for i in range(self._size)]
        for i in range(2*self._n*self._n):
            for k in range(self._n):
                self._trace[i][k]=(1-self._rho)*self._trace[i][k]
        for i in range(self._size):
            for j in range(2*self._n):
                for k in range(self._n):
                    x=j*self._n+k
                    y=self._colony[i].getSolution()[j][k]-1
                    self._trace[x][y]=self._trace[x][y]+pheromoneQ[i]
        f=[[self._colony[i].fitness(self._colony[i].getSolution()),i ]for i in range(self._size) ]
        f=max(f)
        return self._colony[f[1]]
    
    def search(self,nrIters):
        bestAnt=deepcopy(self.iteration())
        for i in range(nrIters-1):
            ant=deepcopy(self.iteration())
            if(ant.fitness(ant.getSolution())<bestAnt.fitness(bestAnt.getSolution())):
                bestAnt=deepcopy(ant)
        return bestAnt
                
            
    
#contr=Controller(3,3,1.9,0.9,0.05,0.5)
#print(contr.iteration())