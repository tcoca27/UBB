from Board import *
from random import choice
from random import randint
import unittest

class Game:
    def __init__(self,ub,cb,ubr,cbr):
        self._ub=ub
        self._cb=cb
        self._ubr=ubr
        self._cbr=cbr

    def ComputerMove(self):
        '''AI for the computer. Shoots randomly if there isn't any ship hit on the user's
        board. If there is, it shoots in the neighbours of that hit'''
        for i in range(8):
            for j in range(8):
                if self._ub._data[i][j] in ['HB','HC','HD']:
                    state=self.ShotifHit(i,j)
                    if state=='hit' or state=='miss':
                        return state
        x=randint(0,7)
        y=randint(0,7)
        state=self._ub.Shot(x,y)
        if state=='hit':
            return 'hit'
        elif state=='miss':
            return 'miss'

    def ShotifHit(self,i,j):
        '''if there's a hit computer picks a random neighbour of that hit'''
        shot=1
        while shot > 0:
            neighbours = [[i - 1, j], [i + 1, j], [i, j - 1], [i, j + 1]]
            point = choice(neighbours)
            state=self._ub.Shot(point[0], point[1])
            if state== 'hit':
                return 'hit'
            if state=='miss':
                return 'miss'
            else: return state

    def PlayerShot(self,x,y,cb):
        '''shoots at the point x,y indicated by the user'''
        state=cb.Shot(x,y)
        return state

    def Start(self):
        '''handles the game. Places ships and shoots until someone wins'''
        dictC={'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7}
        dictR = {'1': 0, '2': 1, '3': 2, '4': 3, '5': 4, '6': 5, '7': 6, '8': 7}
        self.PlacePlayer(self._ub)
        self.PlaceComputer(self._cb)
        while self.isWin(self._cb,self._ub)==False:
            shotc=1
            shotu=1
            while shotc>0:
                state=self.ComputerMove()
                print('User board')
                for i in range(8):
                    for j in range(8):
                        if self._ub._data[i][j] in ['O','X']:
                            self._ubr._data[i][j]=self._ub._data[i][j]
                        elif self._ub._data[i][j] in ['HB','HD','HC']:
                            self._ubr._data[i][j]='H'
                print(self._ubr.__str__())
                if self.isWin(self._cb,self._ub)!=False:
                    print(self.isWin(self._cb,self._ub))
                    return
                if state=='miss':
                    shotc=0
            while shotu>0:
                print('Computer board')
                print(self._cbr.__str__())
                x = (input('Enter row: '))
                y = (input('Enter collumn: '))
                if x not in dictR.keys() or y not in dictC.keys():
                    while x not in dictR.keys() or y not in dictC.keys():
                        print('invalid shot')
                        x = (input('Enter row: '))
                        y = (input('Enter collumn: '))
                x=dictR[x]
                y=dictC[y]
                state=self.PlayerShot(x,y,self._cb)
                print(state)
                print('Computer board')
                for i in range(8):
                    for j in range(8):
                        if self._cb._data[i][j] in ['O','X']:
                            self._cbr._data[i][j]=self._cb._data[i][j]
                        elif self._cb._data[i][j] in ['HB','HD','HC']:
                            self._cbr._data[i][j]='H'
                print(self._cbr.__str__())
                if self.isWin(self._cb,self._ub)!=False:
                    print(self.isWin(self._cb,self._ub))
                    return
                if state=='miss':
                    shotu=0

    def Start2P(self):
        '''same as Start, but for 2 players'''
        dictC = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}
        dictR = {'1': 0, '2': 1, '3': 2, '4': 3, '5': 4, '6': 5, '7': 6, '8': 7}
        self.PlacePlayer(self._ub)
        self.PlacePlayer(self._cb)
        while self.isWin(self._cb, self._ub) == False:
            shotc = 1
            shotu = 1
            while shotc > 0:
                print("Player 1 shoots")
                x = (input('Enter row: '))
                y = (input('Enter collumn: '))
                if x not in dictR.keys() or y not in dictC.keys():
                    while x not in dictR.keys() or y not in dictC.keys():
                        print('invalid shot')
                        x = (input('Enter row: '))
                        y = (input('Enter collumn: '))
                x = dictR[x]
                y = dictC[y]
                state = self.PlayerShot(x, y,self._ub)
                print(state)
                print('Player 2 board')
                for i in range(8):
                    for j in range(8):
                        if self._ub._data[i][j] in ['O', 'X']:
                            self._ubr._data[i][j] = self._ub._data[i][j]
                        elif self._ub._data[i][j] in ['HB', 'HD', 'HC']:
                            self._ubr._data[i][j] = 'H'
                print(self._ubr.__str__())
                if self.isWin(self._cb, self._ub) != False:
                    if self.isWin(self._cb, self._ub)=='Computer wins':
                        print('Player 1 wins')

                    else:
                        print('Player 2 wins')
                    return
                if state == 'miss':
                    shotc = 0
            while shotu > 0:
                print('Player 2 shoots')
                x = (input('Enter row: '))
                y = (input('Enter collumn: '))
                if x not in dictR.keys() or y not in dictC.keys():
                    while x not in dictR.keys() or y not in dictC.keys():
                        print('invalid shot')
                        x = (input('Enter row: '))
                        y = (input('Enter collumn: '))
                x = dictR[x]
                y = dictC[y]
                state = self.PlayerShot(x, y,self._cb)
                print(state)
                print('Player 1 board')
                for i in range(8):
                    for j in range(8):
                        if self._cb._data[i][j] in ['O', 'X']:
                            self._cbr._data[i][j] = self._cb._data[i][j]
                        elif self._cb._data[i][j] in ['HB', 'HD', 'HC']:
                            self._cbr._data[i][j] = 'H'
                print(self._cbr.__str__())
                if self.isWin(self._cb, self._ub) != False:
                    if self.isWin(self._cb, self._ub) == 'Computer wins':
                        print('Player 1 wins')

                    else:
                        print('Player 2 wins')
                    return
                if state == 'miss':
                    shotu = 0

    def PlacePlayer(self,ub):
        '''places all of the user's ships'''
        dictC = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}
        dictR = {'1': 0, '2': 1, '3': 2, '4': 3, '5': 4, '6': 5, '7': 6, '8': 7}
        ships=3
        print(ub.__str__())
        while ships>0:
            if ships==3:
                ship='B'
                alg=input('Enter alignment (v for vertical, h for horizontal) ')
                while alg not in ['v', 'h']:
                    print('not a valid alignment')
                    alg = input('Enter alignment (v for vertical, h for horizontal) ')
                print('Enter start position of the ship ')
                x = (input('Enter row: '))
                y = (input('Enter collumn: '))
                if x not in dictR.keys() or y not in dictC.keys():
                    while x not in dictR.keys() or y not in dictC.keys():
                        print('invalid placement')
                        x = (input('Enter row: '))
                        y = (input('Enter collumn: '))
                x = dictR[x]
                y = dictC[y]
                state = ub._PlaceShip(ship, x, y, alg)
                if state == True:
                    ships -= 1
                    print(ub.__str__())
                else:
                    print(state)
            elif ships==2:
                ship = 'C'
                alg = input('Enter alignment (v for vertical, h for horizontal) ')
                while alg not in ['v', 'h']:
                    print('not a valid alignment')
                    alg = input('Enter alignment (v for vertical, h for horizontal) ')
                print('Enter start position of the ship ')
                x = (input('Enter row: '))
                y = (input('Enter collumn: '))
                if x not in dictR.keys() or y not in dictC.keys():
                    while x not in dictR.keys() or y not in dictC.keys():
                        print('invalid placement')
                        x = (input('Enter row: '))
                        y = (input('Enter collumn: '))
                x = dictR[x]
                y = dictC[y]
                state = ub._PlaceShip(ship, x, y, alg)
                if state == True:
                    ships -= 1
                    print(ub.__str__())
                else:
                    print(state)
            elif ships==1:
                ship = 'D'
                alg = input('Enter alignment (v for vertical, h for horizontal) ')
                while alg not in ['v','h']:
                    print('not a valid alignment')
                    alg = input('Enter alignment (v for vertical, h for horizontal) ')
                print('Enter start position of the ship ')
                x = (input('Enter row: '))
                y = (input('Enter collumn: '))
                if x not in dictR.keys() or y not in dictC.keys():
                    while x not in dictR.keys() or y not in dictC.keys():
                        print('invalid placement')
                        x = (input('Enter row: '))
                        y = (input('Enter collumn: '))
                x = dictR[x]
                y = dictC[y]
                state=ub._PlaceShip(ship, x, y, alg)
                if state== True:
                    ships -= 1
                    print(ub.__str__())
                else:
                    print(state)
        return True


    def PlaceComputer(self,ub):
        '''places all of the computer's ships'''
        ships=3
        algn=['v','h']
        while ships>0:
            if ships==3:
                ship='B'
                alg=choice(algn)
                x=randint(0,7)
                y=randint(0,7)
                state = ub._PlaceShip(ship, x, y, alg)
                if state == True:
                    ships -= 1
            elif ships==2:
                ship = 'C'
                alg = choice(algn)
                x = randint(0, 7)
                y = randint(0, 7)
                state = ub._PlaceShip(ship, x, y, alg)
                if state == True:
                    ships -= 1
            elif ships==1:
                ship = 'D'
                alg = choice(algn)
                x = randint(0, 7)
                y = randint(0, 7)
                state = ub._PlaceShip(ship, x, y, alg)
                if state == True:
                    ships -= 1
        return True


    def isWin(self,cb,ub):
        '''checks if someone won'''
        xc=0
        xu=0
        for i in range(8):
            for j in range(8):
                if self._ub._data[i][j]=='X':
                    xc+=1
                if self._cb._data[i][j]=='X':
                    xu+=1
                if xc==9:
                    return 'Computer wins'
                if xu==9:
                    return 'User wins'
        return False

class Test(unittest.TestCase):
    def setUp(self):
        ub=Board()
        ubr=Board()
        cb=Board()
        cbr=Board()
        self._game=Game(ub,cb,ubr,cbr)

    def tearDown(self):
        self._game=None

    def test(self):
        ub = Board()
        ubr = Board()
        cb = Board()
        cbr = Board()
        self.assertEqual(self._game.PlaceComputer(cb),True)
        self.assertEqual(self._game.isWin(cb,ub),False)
        self.assertEqual(self._game.PlayerShot(1,1,cb),'miss')
        self.assertEqual(self._game.ComputerMove(),'miss')
        self.assertEqual(self._game.PlacePlayer(ub),True)
