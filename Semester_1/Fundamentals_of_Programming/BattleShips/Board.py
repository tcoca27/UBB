from texttable import Texttable
import unittest

class Board:
    def __init__(self):
        self._data=[]
        for i in range(8):
            self._data.append([' ']*8)

    def __str__(self):
        t=Texttable()
        t.header([' ','A','B','C','D','E','F','G','H'])
        for i in range(8):
            t.add_row([i+1]+self._data[i])
        return t.draw()

    def _PlaceShip(self,ship,x,y,aling):
        '''subprogram that tries to place a ship on the board given its allignment and
        starting position '''
        if ship=='B':
            if self.isShip(x,y):
                return ('Ship already placed here')
            else:
                if aling=='v' and x>4:
                    return ('Ship exceeds the map')
                elif aling=='h' and y>4:
                    return ('Ship exceeds the map')
                else:
                    if aling=='v':
                        if self.isShip(x+1,y)==True:
                            return ('Ship already placed here')
                        elif self.isShip(x+2,y)==True:
                            return ('Ship already placed here')
                        elif self.isShip(x+3,y)==True:
                            return ('Ship already placed here')
                        else:
                            self._data[x][y]='B'
                            self._data[x+1][y]='B'
                            self._data[x+2][y]='B'
                            self._data[x+3][y]='B'
                            return True
                    elif aling=='h':
                        if self.isShip(x,y+1)==True:
                            return ('Ship already placed here')
                        elif self.isShip(x,y+2)==True:
                            return ('Ship already placed here')
                        elif self.isShip(x,y+3)==True:
                            return ('Ship already placed here')
                        else:
                            self._data[x][y]='B'
                            self._data[x][y+1]='B'
                            self._data[x][y+2]='B'
                            self._data[x][y+3]='B'
                            return True
                    else:
                        return ('not a valid allignment')
        if ship=='C':
            if self.isShip(x,y):
                return ('Ship already placed here')
            else:
                if aling=='v' and x>5:
                    return ('Ship exceeds the map')
                elif aling=='h' and y>5:
                    return ('Ship exceeds the map')
                else:
                    if aling=='v':
                        if self.isShip(x+1,y)==True:
                            return ('Ship already placed here')
                        elif self.isShip(x+2,y)==True:
                            return ('Ship already placed here')
                        else:
                            self._data[x][y]='C'
                            self._data[x+1][y]='C'
                            self._data[x+2][y]='C'
                            return True
                    elif aling=='h':
                        if self.isShip(x,y+1)==True:
                            return ('Ship already placed here')
                        elif self.isShip(x,y+2)==True:
                            return ('Ship already placed here')
                        else:
                            self._data[x][y]='C'
                            self._data[x][y+1]='C'
                            self._data[x][y+2]='C'
                            return True
                    else:
                        return ('not a valid allignment')
        if ship=='D':
            if self.isShip(x,y):
                return ('Ship already placed here')
            else:
                if aling=='v' and x>6:
                    return ('Ship exceeds the map')
                elif aling=='h' and y>6:
                    return ('Ship exceeds the map')
                else:
                    if aling=='v':
                        if self.isShip(x+1,y)==True:
                            return ('Ship already placed here')
                        else:
                            self._data[x][y]='D'
                            self._data[x+1][y]='D'
                            return True
                    elif aling=='h':
                        if self.isShip(x,y+1)==True:
                            return ('Ship already placed here')
                        else:
                            self._data[x][y]='D'
                            self._data[x][y+1]='D'
                            return True
                    else:
                        return ('not a valid allignment')


    def isShip(self,x,y):
        '''verifies if the point is a ship'''
        if self._data[x][y] in ['B','C','D']:
            return True
        return False

    def Shot(self,x,y):
        '''tries to shoot in the point of coordinates (x,y). Returns hit, miss or invalidity'''
        if x<0 or x>7 or y<0 or y>7:
            return ('invalid shot')
        elif self._data[x][y] in ['C','B','D']:
            hb=0
            hc=0
            hd=0
            if self._data[x][y]=='B':
                self._data[x][y] = 'HB'
                for i in range(8):
                    for j in range(8):
                        if self._data[i][j]=='HB':
                            hb+=1
                if hb==4:
                    for i in range(8):
                        for j in range(8):
                            if self._data[i][j] == 'HB':
                                self._data[i][j]='X'
            elif self._data[x][y]=='C':
                self._data[x][y]='HC'
                for i in range(8):
                    for j in range(8):
                        if self._data[i][j]=='HC':
                            hc+=1
                if hc==3:
                    for i in range(8):
                        for j in range(8):
                            if self._data[i][j] == 'HC':
                                self._data[i][j]='X'
            elif self._data[x][y]=='D':
                self._data[x][y]='HD'
                for i in range(8):
                    for j in range(8):
                        if self._data[i][j]=='HD':
                            hd+=1
                if hb==2:
                    for i in range(8):
                        for j in range(8):
                            if self._data[i][j] == 'HD':
                                self._data[i][j]='X'
            return 'hit'
        elif self._data[x][y]==' ':
            self._data[x][y]='O'
            return 'miss'
        elif self._data[x][y]=='O' or self._data in ['HB', 'HD', 'HC'] or self._data=='X':
            return ("You already shot here")

    def neighboursB(self,x,y):
        '''looks around the neighboors of a ship and returns True if it finds a ship'''
        if x+1<8 and self._data[x+1][y]in ['B','C','D']:
            return True
        if x-1>=0 and self._data[x-1][y]in ['B','C','D']:
            return True
        if y+1<8 and self._data[x][y+1]in ['B','C','D']:
            return True
        if y-1>=0 and self._data[x][y-1]in ['B','C','D']:
            return True
        if y+2<8 and self._data[x][y+2]in ['B','C','D']:
            return True
        if y-2>=0 and self._data[x][y-2]in ['B','C','D']:
            return True
        if x+2<8 and self._data[x+2][y]in ['B','C','D']:
            return True
        if x-2>=0 and self._data[x-2][y]in ['B','C','D']:
            return True
        return False

    def neighbours(self,x,y):
        '''looks around the neighboors of a ship and returns True if it finds a ship'''
        if x+1<8 and self._data[x+1][y] in ['B','C','D']:
            return True
        if x-1>=0 and self._data[x-1][y]in ['B','C','D']:
            return True
        if y+1<8 and self._data[x][y+1]in ['B','C','D']:
            return True
        if y-1>=0 and self._data[x][y-1]in ['B','C','D']:
            return True
        return False


class Test(unittest.TestCase):
    def setUp(self):
        self._board=Board()

    def tearDown(self):
        self._board=None

    def test(self):
        self.assertEqual(self._board._PlaceShip('B',0,0,'v'),True)
        self.assertNotEqual(self._board._PlaceShip('C',7,7,'v'),True)
        self.assertEqual(self._board.isShip(0,0),True)
        self.assertEqual(self._board.isShip(1,1),False)
        self.assertEqual(self._board.Shot(0,0),'hit')
        self.assertEqual(self._board.Shot(0,1),'miss')
        self.assertEqual(self._board.Shot(8,1),'invalid shot')
        self.assertEqual(self._board.neighbours(0,0),True)
        self.assertEqual(self._board.neighbours(2,2),False)

