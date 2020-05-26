from basemodel import BaseModel
from loguru import logger
from peewee import ForeignKeyField, IntegerField, TextField, DoesNotExist
from player import Player
import random
import uuid

def get_player(player_uuid):
    logger.info(f'Searching player with UUID {player_uuid}')
    player = Player.get_or_none(Player.uuid == player_uuid)
    if player:
        logger.info(f'Found player with id {player.id}')
    else:
        logger.info('No player found')
    return player

class Game(BaseModel):
    player1 = ForeignKeyField(Player, backref='games')
    player2 = ForeignKeyField(Player, backref='games', null=True)
    dice = IntegerField(default=-1)
    next_player = ForeignKeyField(Player, backref='games', null=True)
    board = TextField(default='')

    @classmethod
    def find_game(cls, player_uuid):
        logger.info(f'Searching game with player {player_uuid}')
        if (player := get_player(player_uuid)) is None:
            return None
        else:
            game = cls.select().where((cls.player1 == player)|(cls.player2 == player)).get()
            logger.info(f'Found game id {game.id}')
        return game

    @classmethod
    def new_game(cls):
        player = Player()
        player_uuid = str(uuid.uuid4())
        logger.info(f'Created new player. Attempting to assign UUID {player_uuid}')
        while Player.get_or_none(uuid=player_uuid):
            player_uuid = str(uuid.uuid4())
            logger.info(f'UUID exists. Attempting to assign {player_uuid}')
            continue
        player.uuid = player_uuid
        player.save()
        logger.info('New player created')
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

    @classmethod
    def update_board(cls, board):
        game = cls.get(player_uuid)
        if game:
            logger.info(f'Found game {game.id}')
            logger.info(f'Current board {game.board}')
            game.board = board
            game.save()
            logger.info(f'New board {game.board}')
            return True
        else:
            logger.info(f'No game found for player with UUID {player_uuid}')
            return False

    @classmethod
    def throw_dice(cls, player_uuid):
        game = cls.get(player_uuid)
        if game:
            logger.info(f'Found game {game.id}')
            logger.info(f'Current dice value: {game.dice}')
            if game.dice > -1:
                logger.info('Dice was played already, not changing')
                return game.dice
            else:
                dice = []
                for i in range(4):
                    dice.append(random.randint(0,1))
                game.dice = sum(dice)
                logger.info(f'New dice value: {game.dice}')
                logger.info('Saving new dice value')
                game.save()
                logger.info('Game updated with new dice value')
                return game.dice
        else:
            logger.info(f'No game found for player with UUID {player_uuid}')
            return None
