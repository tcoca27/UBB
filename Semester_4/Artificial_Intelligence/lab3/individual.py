# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 15:35:21 2020

@author: tudor
"""

from itertools import permutations
from random import shuffle,random,randint
from copy import deepcopy

class Individual:
    
    def __init__(self, n, geno):
        self._genotype=[]
        self._n=n
        if len(geno)==0:
            self._genotype=(self.createGenotype())
        else:
            self._genotype=geno
        '''pso stuff'''
        self._velocity=[[0 for i in range(n)]for j in range(2*n)]
        self._bestPos=deepcopy(self._genotype)
        self._bestfitness=self.fitness()
        
        
    def getVelocity(self):
        return self._velocity

    def getBestPos(self):
        return self._bestPos
    
    def getBestFit(self):
        return self._bestfitness
    

    def createGenotype(self):
        numbers=[]
        for i in range (1,self._n+1):
            numbers.append(i)
        permutation=[]
        perm=permutations(numbers)
        for p in perm:
            gene=[]
            for value in p:
                gene.append(value)
            permutation.append(gene)
        shuffle(permutation)
        return permutation[:2*self._n]
        
    def buildMatrix(self):
        matrix=[[[0,0] for i in range(self._n)] for j in range(self._n)]
        for i in range(2*self._n):
            for j in range(self._n):
                matrix[i%self._n][j][i//self._n]=self._genotype[i][j]
        return matrix
    
    def prettyPrint(self,matrix):
        s=""
        for i in matrix:
            s+="\n"
            for j in i:
                s+=str(j)
                s+=' '
        return s

    def fitness(self):
        matrix=self.buildMatrix()
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
    
    def mutate(self, probability):
        if probability>random():
            i=randint(0,2*self._n-1)
            shuffle(self._genotype[i])
            
    def setGenotype(self,genotype):
        self._genotype=deepcopy(genotype)
        if self.fitness()<self._bestfitness:
            self._bestPos=deepcopy(genotype)
            self._bestfitness=self.fitness()
    
    def getGenotype(self):
        return self._genotype
        
    def __str__(self):
        s=""
        s+=str(self._genotype)+'\n'+self.prettyPrint(self.buildMatrix())+'\n'
        return s
            
    def getNeighborhood(self):
        geno=deepcopy(self.getGenotype())
        neighborhood=[]
        for i in range(2*self._n):
            shuffle(geno[i])
            neighborhood.append(deepcopy(Individual(self._n,geno)))
            geno=deepcopy(self.getGenotype())
        return neighborhood