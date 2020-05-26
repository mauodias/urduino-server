from models.basemodel import BaseModel
from peewee import TextField, IntegerField
from loguru import logger
import uuid

class Player(BaseModel):
    uuid = TextField()
    total_rocks = IntegerField(default=7)
    active_rocks = IntegerField(default=0)

    @classmethod
    def find(cls, player_uuid):
        logger.info(f'Searching player with UUID {player_uuid}')
        player = cls.get_or_none(cls.uuid == player_uuid)
        if player:
            logger.info(f'Found player with id {player.id}')
        else:
            logger.info('No player found')
        return player

    @classmethod
    def new(cls):
        player = cls()
        player_uuid = str(uuid.uuid4())
        logger.info(f'Created new player. Attempting to assign UUID {player_uuid}')
        while cls.get_or_none(uuid=player_uuid):
            player_uuid = str(uuid.uuid4())
            logger.info(f'UUID exists. Attempting to assign UUID {player_uuid}')
            continue
        player.uuid = player_uuid
        player.save()
        logger.info('New player created')
        return player

    def play_rock(self):
        logger.info(f'Playing rock for player {self.uuid}')
        if self.active_rocks < self.total_rocks:
            logger.info(f'Player had {self.active_rocks} active rocks')
            self.active_rocks += 1
            self.save()
            logger.info(f'Player now has {self.active_rocks} active rocks')
            return True
        logger.info(f'Condition not met, player has active_rocks >= total_rocks')
        return False

    def return_rock(self):
        if self.active_rocks > 0:
            logger.info(f'Player had {self.active_rocks} active rocks')
            self.active_rocks -= 1
            self.save()
            logger.info(f'Player now has {self.active_rocks} active rocks')
            return True
        logger.info(f'Condition not met, player has active_rocks <= 0')
        return False

    def score(self):
        if self.total_rocks > 0 and self.active_rocks > 0:
            logger.info(f'Player had {self.total_rocks} total and {self.active_rocks} active rocks')
            self.total_rocks -= 1
            self.active_rocks -= 1
            self.save()
            logger.info(f'Player now has {self.total_rocks} total and {self.active_rocks} active rocks')
            return True
        logger.info(f'Condition not met, player has active_rocks or total_rocks <= 0')
        return False
