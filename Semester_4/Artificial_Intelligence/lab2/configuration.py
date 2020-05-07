# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 13:27:32 2020

@author: tudor
"""

class Configuration:
    def __init__(self,n,qtuple):
        self._n=n
        self._qtuple=qtuple
        
    def __str__(self):
        s=""
        board=[[0 for i in range(self._n)] for j in range(self._n)]
        for v in self._qtuple:
            board[self._qtuple.index(v)][v]=1
        for row in board:
            for value in row:
                s+=str(value)+" "
            s+='\n'
        return s
    
    def getSize(self):
        return self._n
    
    def getValues(self):
        return self._qtuple
    
    def nextConfig(self):
        nextC=[]
        for col in range(self._n):
            if col not in  self._qtuple:
                if self.valid(col):
                    auxq=self._qtuple[:]
                    auxq.append(col)
                    nextC.append(Configuration(self._n,auxq))
        return nextC

    def valid(self,col):
        aux=self._qtuple[:]
        aux.append(col)
        n=len(aux)
        for i in range(n-1):
            for j in range(i+1,n):
                if j-i==abs(aux[i]-aux[j]):
                    return False
        return True
    
    def __eq__(self,other):
        if not isinstance(other,Configuration):
            return False
        if self._n != other.getSize():
            return False
        for i in range(self._n):
            if self._qtuple[i]!=other.getValues()[i]:
                return False
        return True
        
        