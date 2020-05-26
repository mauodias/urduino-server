from .game import Game
from .player import Player
from loguru import logger
from peewee import SqliteDatabase
import os

logger.info('Initializing database')
db = SqliteDatabase(os.environ.get('DB_PATH', 'db.db'))
logger.info('Creating tables, if needed')
db.create_tables([Player, Game])
