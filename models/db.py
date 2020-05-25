from peewee import *
from connect import db
from player import Player
from game import Game
import random
import uuid

def create_tables():
    db.create_tables([Player, Game])

def update_game(board, player_uuid):
    pass
