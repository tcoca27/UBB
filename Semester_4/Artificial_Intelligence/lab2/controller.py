# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 16:13:03 2020

@author: tudor
"""

from problem import Problem

class Controller:
    def __init__(self,problem):
        self._problem=problem
        
    def DFS(self,root):
        s=[root]
        while len(s)>0:
            currentState=s.pop()
            if len(currentState.getValues()[-1].getValues())==self._problem.getSize():
                return currentState
            s=s+self._problem.expand(currentState)

    def Greedy(self,root):
        q = [root]
        best = 0
        bestState = None
        currentlen = 0
        while len(q)>0:
            while len(q) > 0:
                currentState = q.pop(0)
                if len(currentState.getValues()[-1].getValues()) == self._problem.getSize():
                    return currentState
                if len(currentState.getValues()[-1].getValues()) > currentlen:
                    best = 0
                    currentlen += 1
                if self._problem.heuristics(currentState) >= best:
                    bestState = currentState
                    best = self._problem.heuristics(currentState)
                    q = q + self._problem.expand(bestState) #if a local optimum is found we continue with it
