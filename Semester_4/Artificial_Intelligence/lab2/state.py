# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 13:16:56 2020

@author: tudor
"""

from configuration import Configuration

class State:
    def __init__(self):
        self._values=[]
        
    def setValues(self,values):
        self._values=values
        
    def getValues(self):
        return self._values
    
    def __str__(self):
        s=""
        for value in self._values:
            s+=str(value)+'\n'
        return s
    
    def __add__(self,something):
        aux=State()
        if isinstance(something,State):
            aux.setValues(self._values+something.getValues())
        elif isinstance(something, Configuration):
            aux.setValues(self._values+[something])
        else:
            aux.setValues(self._values)
        return aux    
        