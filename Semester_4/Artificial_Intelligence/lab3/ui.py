# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 02:16:45 2020

@author: tudor
"""

from controller import Controller
from hccontroller import HCcontroller
from psocontroller import PSOController
from population import Population
from random import random
from numpy import mean,array,std
from matplotlib import pyplot as plt

class UI:
    def __init__(self):
        self._controller=Controller(Population(40,3),random())
        self._PSOcontroller=PSOController(Population(40,3),random(),random(),random())
        self._hccontroller=HCcontroller(3)
    
    def run(self):
        while(True):
            print(self.printMenu())
            option=int(input("Input command:"))
            if option==0:
                return
            elif option==1:
                n=int(input("Input side of square:"))
                size=int(input("Input size of population:"))
                prob=float(input("Input probability of mutation:"))
                nrIters=int(input("Input number of iterations:"))
                self._controller=Controller(Population(size,n),prob)
                #fork
                result=self._controller.run(nrIters)
                print("Individual with best fitness:", result[1])
                print("with the fitness=",result[0])
            elif option==2:
                fitness=[]
                for i in range(30):
                    self._controller=Controller(Population(40,3),random())
                    result=self._controller.run(1000)
                    fitness.append(result[0])
                a=array(fitness)
                m=mean(a)
                print("Mean of fitnesses is: ",m)
                sd=std(a)
                print("Standard deviation is: ",sd)
                plt.plot(fitness)
                plt.show()
            elif option==3:
                n=int(input("Input side of the square:"))
                tries=int(input("Input maximum number of climbs:"))
                self._hccontroller=HCcontroller(n)
                result=self._hccontroller.run(tries)
                print("Result:",result[1])
                print("with the fitness=",result[0])
            elif option==4:
                nrIters=int(input("Input number of iterations:"))
                result=self._controller.run(nrIters)
                print("Individual with best fitness:", result[1])
                print("with the fitness=",result[0])
            elif option==5:
                n=int(input("Input side of square:"))
                size=int(input("Input size of population:"))
                w=float(input("Input inertia coefficient:"))
                c1=float(input("Input cognitive learning coefficient:"))
                c2=float(input("Input social learning coefficient:"))
                nrIters=int(input("Input number of iterations:"))
                self._PSOcontroller=PSOController(Population(size,n),w,c1,c2)
                result=self._PSOcontroller.run(nrIters)
                print("Individual with best fitness:", result[1])
                print("with the fitness=",result[0])
            elif option==6:
                nrIters=int(input("Input number of iterations:"))
                result=self._PSOcontroller.run(nrIters)
                print("Individual with best fitness:", result[1])
                print("with the fitness=",result[0])
            elif option==7:
                fitness=[]
                for i in range(30):
                    self._PSOcontroller=PSOController(Population(40,3),random(),random(),random())
                    result=self._PSOcontroller.run(100)
                    fitness.append(result[0])
                a=array(fitness)
                m=mean(a)
                print("Mean of fitnesses is: ",m)
                sd=std(a)
                print("Standard deviation is: ",sd)
                plt.plot(fitness)
                plt.show()
            else:
                print("Wrong command")
            

                
    def printMenu(self):
        s="\nCommand menu: \n0.Exit\n1.Run EA with new parameters\n2.Statistical validation\n3.Run Hill Climbing algorithm\n4.Run EA with existing parameters\n"
        s+="5.Run PSO with new parameters\n6.Run PSO with existing parameters\n7.Statistical validation PSO\n"
        return s
    
    
ui=UI()
ui.run()