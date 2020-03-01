import random

class Game:
    
    def __init__(self):
        X='x'
        self._board = [[0,0,0],
                       [0,0,0],
                       [X,0,X],
                       [X,0,X],
                       [0,0,0],
                       [0,0,0],
                       [0,0,0],
                       [0,0,0]]

    @property
    def board(self):
        b = ''
        for row in self._board:
            for cell in row:
                b = b + str(cell)
        return b

def draw():
    dice = []
    for i in range(4):
        dice.append(random.randint(0,1))
    return str(sum(dice))
