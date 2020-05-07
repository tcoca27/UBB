# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 23:19:06 2020

@author: tudor
"""

from population import Population
from copy import deepcopy
from random import random,randint

class PSOController:
    def __init__(self,population,w,c1,c2):
        self._population=population
        self._neighbours=population.selectNeighbours(randint(1,population.getN()-1))
        self._w=w
        self._c1=c1
        self._c2=c2
        
    def iteration(self):
        bestNeighbours=[]
        size=self._population.getSize()
        n=self._population.getN()
        pop=deepcopy(self._population.getIndividuals())
        
        for i in range(size):
            bestNeighbours.append(self._neighbours[i][0])
            for j in range(1,len(self._neighbours[i])):
                if(pop[bestNeighbours[i]].fitness()>pop[self._neighbours[i][j]].fitness()):
                    bestNeighbours[i]=self._neighbours[i][j]
                    
        for i in range(size):
            for j in range(len(pop[i].getVelocity())):
                r1=random()
                r2=random()
                for k in range(len(pop[i].getVelocity()[j])):
                    newVelocity=self._w*pop[i].getVelocity()[j][k]
                    newVelocity+=self._c1 * r1 * (pop[bestNeighbours[i]].getGenotype()[j][k]-pop[i].getGenotype()[j][k])
                    newVelocity+=self._c2 * r2 * (pop[i].getBestPos()[j][k]-pop[i].getGenotype()[j][k])
                    newVelocity=int(newVelocity)
                    pop[i].getVelocity()[j][k]=newVelocity
                    
        for i in range(size):
            newPos=[]
            for j in range(len(pop[i].getVelocity())):
                newPosInner=[]
                for k in range(len(pop[i].getVelocity()[j])):
                    adder=pop[i].getGenotype()[j][k]+pop[i].getVelocity()[j][k]
                    if adder<1:
                        adder=1
                    if adder>n:
                        adder=n
                    newPosInner.append(adder)
                newPos.append(deepcopy(newPosInner))
            pop[i].setGenotype(newPos)
        return pop
    
    def run(self, noIters):
        for i in range(noIters):
            self._population.setIndividuals(self.iteration())
        graded=deepcopy(self._population.getIndividuals())
        graded.sort(key=lambda x: x.fitness())
        result=[graded[0].fitness(),graded[0]]
        return result
            
            
                    
                    