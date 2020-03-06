from Game import *

class UI:
    def __init__(self,game):
        self._game=game

    def Start(self):
        inp=input('Do you want to play against the computer or pvp? (c for computer, p for player) ')
        while inp not in ['c','p']:
            print('Wrong input')
            inp = input('Do you want to play against the computer or pvp? (c for computer, p for player) ')
        try:
            if inp=='c':
                self._game.Start()
            elif inp=='p':
                self._game.Start2P()
            else:
                print('Wrong input')
        except Exception as e:
            print(e)

cbr=Board()
ubr=Board()
ub=Board()
cb=Board()
gm=Game(ub,cb,ubr,cbr)
ui=UI(gm)
ui.Start()
