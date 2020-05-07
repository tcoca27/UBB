# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 16:29:30 2020

@author: tudor
"""

from configuration import Configuration
from problem import Problem
from controller import Controller

class UI:
    def __init__(self):
        self._initial=Configuration(4,[])
        self._problem=Problem(self._initial)
        self._controller=Controller(self._problem)
        
    def printMenu(self):
        s = ''
        s += "0 - exit \n"
        s += "1 - read n (default is 4) \n"
        s += "2 - find a path with DFS \n"
        s += "3 - find a path with Greedy \n"
        print(s)
        
    def start(self):
        while True:
            self.printMenu()
            c=input("Input command:")
            if c=='0':
                return
            elif c=='1':
                n=int(input("input new n:"))
                self._initial=Configuration(n,[])
                self._problem=Problem(self._initial)
                self._controller=Controller(self._problem)
            elif c=='2':
                self.runDFS()
            elif c=='3':
                self.runGreedy()
            else:
                print("wrong input")
    
    def runDFS(self):
        print(str(self._controller.DFS(self._problem.getRoot())))

    def runGreedy(self):
        print(str(self._controller.Greedy(self._problem.getRoot())))
        
ui=UI()
ui.start()