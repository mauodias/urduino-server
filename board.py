from loguru import logger

class Track:
    def __init__(self):
        self.start = [0]*4
        self.end = [0]*2

class Move:
    def __init__(self, success, rosette=False, captured=False):
        self._success = bool(success)
        self._rosette = bool(rosette)
        self._captured = bool(captured)
        pass

    @property
    def success(self):
        return self._success

    @property
    def rosette(self):
        return self._rosette

    @property
    def captured(self):
        return self._captured

class Board:
    def __init__(self):
        self.common = [0]*8
        self.player_track = [None, Track(), Track()]

    def move(self, player, position, count):
        logger.debug(f'Entered move with player: {player}, position: {position}, count: {count}')
        if count == 0:
            logger.debug('Count is 0, not moving')
            return Move(False)
        final_position = position + count
        common = final_position >= 4 and final_position < 12
        logger.debug(f'Final position is {final_position}')
        logger.debug(f'Player is{"" if common else " not"} in the common track')
        if final_position < 4:
            move_track = self.player_track[player].start
            rosette = 3
            logger.debug('Player is in the start track')
        elif final_position < 12:
            move_track = self.common
            final_position -= 4
            rosette = 4
            logger.debug(f'Player is in the common track, position adjusted to {final_position}')
        elif final_position < 14:
            move_track = self.player_track[player].end
            final_position -= 12
            rosette = 0
            logger.debug(f'Player is in the end track, position adjusted to {final_position}')
        else:
            logger.debug('Final position exceeded board, not moving')
            return Move(False)
        is_rosette = final_position == rosette
        captured = False
        if move_track[final_position] == player:
            logger.debug('Player already has a rock in the same position')
            move_success = False
        else:
            if not common:
                move_track[final_position] = player
                move_success = True
                logger.debug('Player positioned out of the common track')
            else:
                if move_track[final_position] != 0:
                    if is_rosette:
                        move_success = False
                        logger.debug('Rosette in the common track is not free, not moving')
                    else:
                        move_track[final_position] = player
                        move_success = True
                        captured = True
                        logger.debug('Player captured an oponent rock in the common track')
                else:
                    move_track[final_position] = player
                    move_success = True
                    logger.debug('Player positioned in the common track')
        logger.debug(f'Move did{"" if move_success else " not"} succeed, player is{"" if is_rosette else " not"} in a rosette and did{"" if captured else " not"} capture another rock')
        return Move(move_success, is_rosette, captured)

    @property
    def matrix(self):
        top = self.player_track[2].start[::-1]
        top.extend([None, None])
        top.extend(self.player_track[2].end[::-1])
        bottom = self.player_track[1].start[::-1]
        bottom.extend([None, None])
        bottom.extend(self.player_track[1].end[::-1])
        return [top, self.common, bottom]

