# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 17:51:07 2020

@author: tudor
"""

from individual import Individual
from random import randint
from copy import deepcopy

class Population:
    def __init__(self, size, n):
        self._size=size
        self._n=n
        self._individuals=self.generatePopulation()
        
    def getIndividuals(self):
        return self._individuals
    
    def setIndividuals(self,individuals):
        self._individuals=individuals
    
    def getSize(self):
        return self._size
    
    def getN(self):
        return self._n
        
    def generatePopulation(self):
        result=[]
        for i in range(self._size):
            individual=Individual(self._n,[])
            result.append(individual)
        return result
    
    def crossover(self,parent1,parent2):
        children=[]
        cut1=randint(1,self._n*2 -2)
        cut2=randint(1,self._n*2 -2)
        while cut1==cut2:
            cut2=randint(1,self._n*2 -2)
        if cut1>cut2:
            cut1, cut2=cut2, cut1
        geno1=parent1.getGenotype()[:cut1]+parent2.getGenotype()[cut1:cut2]+parent1.getGenotype()[cut2:]
        geno2=parent2.getGenotype()[:cut1]+parent1.getGenotype()[cut1:cut2]+parent2.getGenotype()[cut2:]
        child1=Individual(self._n,geno1)
        child2=Individual(self._n,geno2)
        children.append(child1)
        children.append(child2)
        return children

    def selectNeighbours(self,nrNeighbours):
        neighbours=[]
        for i in range(self._size):
            localNeighbours=[]
            for j in range(nrNeighbours):
                index=randint(0,self._size-1)
                while index in localNeighbours:
                    index=randint(0,self._size-1)
                localNeighbours.append(index)
            neighbours.append(deepcopy(localNeighbours))
        return neighbours
    

#i1=Individual(3)
#i2=Individual(3)
#p=Population(1,5,3)
#p.crossover(i1, i2)

        
        
        