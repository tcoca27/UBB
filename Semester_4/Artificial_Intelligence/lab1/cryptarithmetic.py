# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 21:27:35 2020

@author: tudor
"""

import random

class Cryptarithmetic:
    def __init__(self,filename):
        self._letters=[]
        self._firstletters=[]
        self._operand1=[]
        self._operand2=[]
        self._result=[]
        self._operator=''
        self.readFile(filename)
        
    def readFile(self,filename):
        op=1
        count=0
        file=open(filename,'r')
        for line in file:
            for char in line:
                if char=='+' or char=='-':
                    self._operator=char
                    op+=1
                    count=0
                elif char=='=':
                    op+=1
                    count=0
                else:
                    if count==0:
                        self._firstletters.append(char)
                        count=1
                    if self._letters.count(char)==0:
                        self._letters.append(char)
                    if(op==1):
                        self._operand1.append(char)
                    elif(op==2):
                        self._operand2.append(char)
                    else:
                        self._result.append(char)
    
    def show(self):
        print(self._operand1,self._operator,self._operand2,"=",self._result)
                
                
    def solve(self,attempts):
        print("searching solution for: ")
        self.show()
        count=1
        while count<=attempts:
            print("attempt number ",count)
            values={}
            for letter in self._letters:
                values[letter]=random.randint(0,15)
            for letter in self._firstletters:
                values[letter]=random.randint(1,15)                
            #values={'M':1,'O':0,'N':11,'R':0,'D':4,'E':11,'Y':15,'S':15}
            if self._operator=='+':
                if(self.checkAdd(values)):
                    print("solution found on attempt ",count)
                    print(values)
                    break
            if self._operator=='-':
                if(self.checkDiff(values)):
                    print("solution found on attempt ",count)
                    print(values)
                    break
            count+=1
    
    def checkAdd(self,values):
        n1=len(self._operand1)-1
        n2=len(self._operand2)-1
        nr=len(self._result)-1
        carry=0
        while(n1>=0 and n2>=0):
            r=values[self._operand1[n1]]+values[self._operand2[n2]]+carry
            carry=int(r/16)
            r=r%16
            if(values[self._result[nr]]!=r):
                return False
            n1-=1
            n2-=1
            nr-=1
        while(n1>=0):
            r=values[self._operand1[n1]]+carry
            carry=int(r/16)
            r=r%16
            if(values[self._result[nr]]!=r):
                return False
            n1-=1
            nr-=1
        while(n2>=0):
            r=values[self._operand1[n2]]+carry
            carry=int(r/16)
            r=r%16
            if(values[self._result[nr]]!=r):
                return False
            n2-=1
            nr-=1
        if(carry>=0):
            if(values[self._result[nr]]!=carry):
                return False
            carry=0
            nr-=1
        return True
        
    def computeDiff(self,values):
        n1=len(self._operand1)-1
        n2=len(self._operand2)-1
        nr=len(self._result)-1
        carry=0
        while(n1>=0 and n2>=0):
            r=values[self._operand1[n1]]-values[self._operand2[n2]]+carry
            if(r<0):
                carry=-1
                r=abs(r)
            r=r%16
            if(values[self._result[nr]]!=r):
                return False
            n1-=1
            n2-=1
            nr-=1
        while(n1>=0):
            r=values[self._operand1[n1]]+carry
            if(r<0):
                carry=-1
                r=abs(r)
            r=r%16
            if(values[self._result[nr]]!=r):
                return False
            n1-=1
            nr-=1
        while(n2>=0):
            r=values[self._operand1[n2]]+carry
            if(r<0):
                carry=-1
                r=abs(r)
            r=r%16
            if(values[self._result[nr]]!=r):
                return False
            n2-=1
            nr-=1
        if(carry>=0):
            if(values[self._result[nr]]!=carry):
                return False
            carry=0
            nr-=1
        return True
                
#ca=Cryptarithmetic("ca.txt")
#ca.solve(100000)
#print(ca.checkAdd({'M':1,'O':0,'N':11,'R':0,'D':4,'E':11,'Y':15,'S':15}))
