# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 20:40:05 2020

@author: tudor
"""

from numpy import mean,array,std
from matplotlib import pyplot as plt

from controller import Controller

class UI:
    def __init__(self):
        self._controller=Controller(10,3,1.9,0.9,0.05,0.5)
        
    def printMenu(self):
        s="0.Exit\n1.Run ACO with new parameters\n2.Run ACO with existing parameters\n3.Statistical validation\n"
        return s
        
    def start(self):
         while(True):
            print(self.printMenu())
            option=int(input("Input command:"))
            if option==0:
                return
            elif option==1:
                size=int(input("Input number of ants:"))
                n=int(input("Input side of square:"))
                alpha=float(input("Input alpha:"))
                beta=float(input("Input beta:"))
                q0=float(input("Input q0:"))
                degradation=float(input("Input degradation factor:"))
                nrIters=int(input("Input number of iterations:"))
                self._controller=Controller(size,n,alpha,beta,q0,degradation)
                result=self._controller.search(nrIters)
                self.printBestSol(result)
            elif option==2:
                nrIters=int(input("Input number of iterations:"))
                result=self._controller.search(nrIters)
                self.printBestSol(result)
            elif option==3:
                fitness=[]
                for i in range(30):
                    self._controller=Controller(10,3,1.9,0.9,0.05,0.5)
                    result=self._controller.search(100)
                    fitness.append(result.fitness(result.getSolution()))
                a=array(fitness)
                m=mean(a)
                print("Mean of fitnesses is: ",m)
                sd=std(a)
                print("Standard deviation is: ",sd)
                plt.plot(fitness)
                plt.show()
                
    def printBestSol(self,ant):
        print("Best found solution:")
        print(ant.prettyPrint(ant.buildMatrix(ant.getSolution())))
        print("\nWith fitness: ",ant.fitness(ant.getSolution()),'\n')
        
ui= UI()
ui.start()