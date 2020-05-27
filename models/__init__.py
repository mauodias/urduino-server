from .game import Game
from .player import Player
from loguru import logger
from .connect import db

logger.info('Creating tables, if needed')
db.create_tables([Player, Game])
