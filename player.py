import uuid

class Player:

    def __init__(self):
        self._id = uuid.uuid4()
        self._gameid = -1
        self._total_rocks = 7
        self._active_rocks = 0

    @property
    def total_rocks(self):
        return self._total_rocks

    @property
    def active_rocks(self):
        return self._active_rocks

    @property
    def gameid(self):
        return self._gameid

    @gameid.setter
    def gameid(self, value):
        self._gameid = value

    def play_rock(self):
        if self.active_rocks < self.total_rocks:
            self._active_rocks += 1
            return True
        return False

    def recover_rock(self):
        if self.active_rocks > 0:
            self._active_rocks -= 1
            return True
        return False

    def complete_lap(self):
        if self.total_rocks > 0 and self.active_rocks > 0:
            self._active_rocks -= 1
            self._total_rocks -= 1
            return True
        return False
