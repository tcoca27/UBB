# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 23:46:27 2020

@author: tudor
"""

from sudoku import Sudoku
from cryptarithmetic import Cryptarithmetic
from geometricForms import GeometricForms

def printMenu():
    print("Commands:")
    print("0.Exit")
    print("1.Sudoku")
    print("2.Cryptarithmetic")
    print("3.Geometric Forms")

def Start():
    while True:
        printMenu()
        com=input("input command:")
        if com=='0':
            break
        if com=='1':
            filename=input('give filename for the sudoku:')
            sud=Sudoku(filename)
            attempts=int(input('give number of attempts:'))
            sud.solve(attempts)
        if com=='2':
            filename=input('give filename for the sudoku:')
            ca=Cryptarithmetic(filename)
            attempts=int(input('give number of attempts:'))
            ca.solve(attempts)
        if com=='3':
            gf=GeometricForms()
            attempts=int(input('give number of attempts:'))
            gf.solve(attempts)                                    
            
Start()