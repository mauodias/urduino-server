from basemodel import BaseModel
from peewee import TextField, IntegerField

class Player(BaseModel):
    player_uuid = TextField()
    rocks_left = IntegerField(default=7)

    @classmethod
    def less_rocks(cls, player_uuid):
        player = cls.select().where(cls.player_uuid == player_uuid).get()
        player.rocks_left -= 1
        player.save()
