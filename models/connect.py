from loguru import logger
from peewee import SqliteDatabase
import os

logger.info('Initializing database')
db = SqliteDatabase(os.environ.get('DB_PATH', 'db.db'))
