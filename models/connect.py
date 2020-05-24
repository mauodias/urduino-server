from peewee import SqliteDatabase
import os

db = SqliteDatabase(os.environ.get('DB_PATH', 'db.db'))
