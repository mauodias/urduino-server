from basemodel import BaseModel
from peewee import ForeignKeyField, IntegerField, TextField
from player import Player

class Game(BaseModel):
    player1 = ForeignKeyField(Player, backref='games')
    player2 = ForeignKeyField(Player, backref='games', null=True)
    dice = IntegerField(default=-1)
    next_player = ForeignKeyField(Player, backref='games', null=True)
    board = TextField(default='')
