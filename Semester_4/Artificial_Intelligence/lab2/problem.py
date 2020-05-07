# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 13:06:33 2020

@author: tudor
"""

from state import State
from configuration import Configuration

class Problem:
    def __init__(self,initialConfig):
        self._n=initialConfig.getSize()
        self._initialConfig=initialConfig
        self._initialState=State()
        self._initialState.setValues([self._initialConfig])
        
    def getRoot(self):
        return self._initialState
    
    def getSize(self):
        return self._n
    
    def expand(self,current):
        expanded=[]
        currentConfig=current.getValues()[-1]
        for x in currentConfig.nextConfig():
            expanded.append(current+x)
        return expanded
    
    def heuristics(self,state):
        '''the score of a state is given by how many valid positions there are left on the board'''
        currentConfig=state.getValues()[-1]
        n=currentConfig.getSize()
        matrix=self.buildMatrix(currentConfig.getSize(),currentConfig.getValues())
        count=self.countValids(matrix)
        return count

    def buildMatrix(self,size,tuple):
        board=[[0 for i in range(self._n)] for j in range(self._n)]
        for v in tuple:
            board[tuple.index(v)][v]=1
        return board

    def countValids(self,matrix):
        n=len(matrix)
        count=0
        for i in range(n):
            for j in range(n):
                if self.valid(matrix,i,j):
                    count+=1
        return count

    def valid(self,matrix,row,col):
        if matrix[row][col]==1:
            return False
        n=len(matrix)
        for i in range (n):
            if matrix[i][col]==1:
                return False
            if matrix[row][i]==1:
                return False
        rup,cup=row+1,col+1
        rdown,cdown=row-1,col-1
        while (rup<n and cup <n):
            if matrix[rup][cup]==1:
                return False
            rup+=1
            cup+=1
        while rdown>=0 and cdown>=0:
            if matrix[rdown][cdown]==1:
                return False
            rdown-=1
            cdown-=1
        rup, cup = row + 1, col + 1
        rdown, cdown = row - 1, col - 1
        while rup<n and cdown>=0:
            if matrix[rup][cdown]==1:
                return False
            rup+=1
            cdown-=1
        while cup<n and rdown>=0:
            if matrix[rdown][cup]==1:
                return False
            rdown-=1
            cup+=1
        return True