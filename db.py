from peewee import *
import configparser
import random
import uuid

config = configparser.ConfigParser()
config.read('config.ini')
connection = SqliteDatabase(config['db']['path'])

class BaseModel(Model):
    class Meta:
        database = connection

class Player(BaseModel):
    player_uuid = TextField()
    rocks_left = IntegerField(default=7)

class Game(BaseModel):
    player1 = ForeignKeyField(Player, backref='games')
    player2 = ForeignKeyField(Player, backref='games', null=True)

class DB:

    def __init__(self):
        connection.create_tables([Player, Game])

    def new_game(self):
        with connection:
            player = Player()
            player_uuid = str(uuid.uuid4())
            while Player.get_or_none(player_uuid=player_uuid):
                player_uuid = str(uuid.uuid4())
                continue
            player.player_uuid = player_uuid
            player.save()
            available_games = Game.select().where(Game.player2 == None)
            if available_games.count() == 0:
                game = Game(player1=player)
            else:
                game = available_games.first()
                game.player2 = player
            game.save()
            return player, game

    def get_game(self, player_uuid):
        with connection:
            player = Player.get(Player.player_uuid==player_uuid)
            game = Game.select().where((Game.player1 == player)|(Game.player2 == player)).get()
            return game

    def update_game(self, board, player_uuid):
        pass
