# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 23:10:45 2020

@author: tudor
"""

import random

class GeometricForms:
    def __init__(self):
        self._board=[[0 for i in range(6)] for j in range(5)] 
        
    def show(self):
        for row in self._board:
            for value in row:
                print(value,end=" ")
            print('\n')
            
    def addLine(self):
        x=random.randint(0,4)
        y=random.randint(0,2)
        for i in range(y,y+4):
            self._board[x][i]+=1
    
    def addU(self):
        x=random.randint(1,4)
        y=random.randint(0,3)
        self._board[x-1][y]+=1
        self._board[x-1][y+2]+=1
        for i in range(y,y+3):
            self._board[x][i]+=1
    
    def addT(self):
        x=random.randint(1,4)
        y=random.randint(0,3)
        self._board[x-1][y+1]+=1
        for i in range(y,y+3):
            self._board[x][i]+=1
        
    def addLU(self):
        x=random.randint(1,4)
        y=random.randint(0,3)
        self._board[x-1][y]+=1
        for i in range(y,y+3):
            self._board[x][i]+=1
            
    def addLD(self):
        x=random.randint(0,3)
        y=random.randint(0,3)
        self._board[x+1][y+2]+=1
        for i in range(y,y+3):
            self._board[x][i]+=1
            
    def solve(self,attempts):
        count=1
        while(count<=attempts):
            sol=True
            print("attempt number ",count)
            self.addLine()
            self.addLD()
            self.addLU()
            self.addT()
            self.addU()
            for row in self._board:
                for value in row:
                    if value>1:
                        sol=False
            if(sol):
                print("solution found on attempt ",count)
                self.show()
                break
            count+=1
            self._board=[[0 for i in range(6)] for j in range(5)] 

        
#gf=GeometricForms()
#gf.solve(1000)