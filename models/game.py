from models.basemodel import BaseModel
from models.player import Player
from loguru import logger
from peewee import ForeignKeyField, IntegerField, TextField, DoesNotExist
import random
import uuid

class Game(BaseModel):
    player1 = ForeignKeyField(Player, backref='games')
    player2 = ForeignKeyField(Player, backref='games', null=True)
    dice = IntegerField(default=-1)
    next_player = ForeignKeyField(Player, backref='games', null=True)
    board = TextField(default='')

    @classmethod
    def find(cls, player):
        logger.info(f'Searching game with player {player.uuid}')
        game = cls.select().where((cls.player1 == player)|(cls.player2 == player)).get()
        logger.info(f'Found game id {game.id}')
        return game

    @classmethod
    def new(cls):
        player = Player.new()
        try:
            game = cls.select().where(cls.player2 == None).get()
            logger.info(f'Found game id {game.id} with an empty slot. Assigning to player UUID {player.uuid}')
            game.player2 = player
        except cls.DoesNotExist:
            logger.info('No available games found, creating new.')
            game = cls(player1=player)
        game.save()
        logger.info(f'Game id {game.id} saved')
        return game

    def update_board(self, board):
        logger.info(f'Updating game {game.id}')
        logger.info(f'Current board {game.board}')
        self.board = board
        self.save()
        logger.info(f'Board updated to {game.board}')
        return True

    def throw_dice(self):
        logger.info(f'Throwing dice for game {self.id}')
        logger.info(f'Current value: {self.dice}')
        if self.dice > -1:
            logger.info('Dice was played already, not changing')
            return self.dice
        else:
            dice = []
            for i in range(4):
                dice.append(random.randint(0,1))
            self.dice = sum(dice)
            logger.info(f'New dice value: {self.dice}')
            logger.info('Saving new dice value')
            self.save()
            logger.info('Game updated with new dice value')
            return self.dice
