from connect import db
from peewee import Model

class BaseModel(Model):
    class Meta:
        database = db
