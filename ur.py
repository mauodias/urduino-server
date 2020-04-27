from loguru import logger
import random
import uuid

from board import Board

class Game:
    
    def __init__(self):
        self._id = uuid.uuid4()
        self._board = Board()
        #self._player_top = Player()
        #self._player_bottom = Player()

    @property
    def player_top(self):
        return self._player_top.id

    @property
    def player_bottom(self):
        return self._player_bottom.id

    def throw_dice(self):
        dice = []
        for i in range(4):
            dice.append(random.randint(0,1))
        return str(sum(dice))
