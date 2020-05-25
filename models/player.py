from basemodel import BaseModel
from peewee import TextField, IntegerField

class Player(BaseModel):
    uuid = TextField()
    total_rocks = IntegerField(default=7)
    active_rocks = IntegerField(default=0)

    @classmethod
    def less_rocks(cls, player_uuid):
        player = cls.select().where(cls.player_uuid == player_uuid).get()
        player.rocks_left -= 1
        player.save()

    @classmethod
    def play_rock(cls, player_uuid):
        player = cls.select().where(cls.player_uuid == player_uuid).get_or_none()
        if player:
            if player.active_rocks < player.total_rocks:
                player.active_rocks += 1
                player.save
                return True
        return False
