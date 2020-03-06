# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 13:56:00 2020

@author: tudor
"""
import random
import math
from copy import deepcopy

class Sudoku:
    def __init__(self,filename):
        self._board=[]
        self._board=self.readFile(filename)
        self._copy=self.readFile(filename)
            
    def show(self):
        for row in self._board:
            for val in row:
                print(val,end=" ")
            print('\n')
            
    def getN(self):
        return len(self._board)
        
    def readFile(self,filename):
        file=open(filename,'r')
        board=[[int(num) for num in line.split(" ")] for line in file]
        return board
    
    def check_rows(self):
        for row in self._board:
            for value in row:
                if row.count(value)!=1:
                    return False
        return True
    
    def check_collumns(self):
        for row in range(0,self.getN()):
            numbers=[]
            for col in range(0,self.getN()):
                if numbers.count(self._board[row][col])==1:
                    return False
                else:
                    numbers.append(self._board[row][col])
        return True
    
    
    def check_boxes(self):
        s = int(math.sqrt(len(self._board)))
        for row in range(0, self.getN(), s):
            for col in range(0, self.getN(), s):
                 temp = []
                 for r in range(row, row + s):
                    for c in range(col, col + s):
                        temp.append(self._board[r][c])
                 if len(temp) != len(set(temp)):
                     return False
        return True


            
    def is_solution(self):
        return self.check_boxes() and self.check_collumns() and self.check_rows()
    
    def next_to_fill(self):
        for row in self._board:
            for value in row:
                if value == 0:
                    r=self._board.index(row)
                    c=row.index(value)
                    return r,c
        return -1,-1
    
    def solve(self,attempts):
        print("Searching solution for")
        self.show()
        print('\n')
        count=1
        while count<=attempts:
            row,col=0,0
            while row!=-1:
                row,col=self.next_to_fill()
                x=random.randint(1,self.getN())
                self._board[row][col]=x
            if(self.is_solution()):
                self.show()
                print("Solution found in ",count," attempts")
                break
            else:
                print("Attempt number ",count,'\n')
                self._board=deepcopy(self._copy)
            count+=1
        
       
        
#sud=Sudoku('sudoku9.txt')
#sud.solve(10000)