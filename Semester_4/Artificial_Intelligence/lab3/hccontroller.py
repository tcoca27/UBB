# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 19:38:08 2020

@author: tudor
"""

from individual import Individual

class HCcontroller:
    def __init__(self,n):
        self._bestIndiv=Individual(n,[])
        
    def run(self,nrTries):
        while(nrTries>0) and self._bestIndiv.fitness()>0:
            neighborhood=self._bestIndiv.getNeighborhood()
            neighborhood.sort(key=lambda x: x.fitness())
            self._bestIndiv=neighborhood[0]
            nrTries-=1
        return [self._bestIndiv.fitness(),self._bestIndiv]
