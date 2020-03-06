# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy
import matplotlib.pyplot as plt    
    

def PrintCommands():
    print("Commands menu: \t")
    print("0.Exit \t")
    print("1.Binomial Distribution \t")
    print("2.Uniform Distribution \t")
    
def Binomial(n,p,size):
    numbers=[]
    numbers=numpy.random.binomial(n,p,size)
    plt.plot(numbers,'ro')
    plt.show()


def Uniform(low,high,size):
    numbers=[]
    numbers=numpy.random.uniform(low,high,size)
    plt.plot(numbers,'ro')
    plt.show()
    
def start():
    while True:
        PrintCommands()
        userInput=input("Command:")
        if userInput=='0':
            break
        elif userInput=='1':
            n=int(input("N:"))
            p=float(input("probability:"))
            size=int(input("size:"))
            Binomial(n,p,size)
        elif userInput=='2':
            low=float(input("low:"))
            high=float(input("high:"))
            size=int(input("size:"))
            Uniform(low,high,size)

start()

            