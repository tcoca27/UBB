# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 18:22:51 2020

@author: tudor
"""

from random import randint
from population import Population
from copy import deepcopy


class Controller:
    def __init__(self, population, prob):
        self._population=population
        self._probability=prob
        
    def iteration(self):
        pop=deepcopy(self._population.getIndividuals())
        i1=randint(0,len(pop)-1)
        i2=randint(0,len(pop)-1)
        while(i1==i2):
            i2=randint(0,len(pop)-1)
        if (i1!=i2):
            children=self._population.crossover(pop[i1],pop[i2])
            child1=children[0]
            child2=children[1]
            child1.mutate(self._probability)
            child2.mutate(self._probability)
            f1=pop[i1].fitness()
            f2=pop[i2].fitness()
            fc1=child1.fitness()
            fc2=child2.fitness()
            if(f1>f2):
                if fc1<fc2:
                    if f1>=fc1:
                        pop[i1]=child1
                        if f2>=fc2:
                            pop[i2]=child2
                else:
                    if f1>=fc2:
                        pop[i1]=child2
                        if f2>=fc1:
                            pop[i2]=child1
            else:
                if fc1<fc2:
                    if f2>=fc1:
                        pop[i2]=child1
                        if f1>=fc2:
                            pop[i1]=child2
                else:
                    if f2>=fc2:
                        pop[i2]=child2
                        if f1>=fc1:
                            pop[i1]=child1
        return pop
    
    def run(self,nrIters):
        for i in range(nrIters):
            self._population.setIndividuals(self.iteration())
        graded=deepcopy(self._population.getIndividuals())
        graded.sort(key=lambda x: x.fitness())
        result=[graded[0].fitness(),graded[0]]
        return result
            
    
#p=Population(5,3)
#c=Controller(p,0.4)
#result=c.run(5)
#print(result[0])
#print(result[1])
