from peewee import *
from connect import db
from player import Player
from game import Game
import random
import uuid

def create_tables():
    db.create_tables([Player, Game])

def new_game():
    with db:
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

def get_game(player_uuid):
    with db:
        player = Player.get(Player.player_uuid==player_uuid)
        game = Game.select().where((Game.player1 == player)|(Game.player2 == player)).get()
        return game

def update_game(board, player_uuid):
    pass
