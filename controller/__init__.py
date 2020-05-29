from loguru import logger
import json
import models

class Payload:
    def __init__(self, success, data, message=None):
        self.success = success
        self.data = data
        if success and not message:
            self.message = 'success'
        else:
            self.message = message

def dice(uuid):
    logger.info(f'Received dice request with ID {uuid}')


    # dummy dice result. Here goes call to models
    dice_result = 4


    logger.info(f'Obtained value {dice_result}')
    data = {'value': dice_result}
    response = Payload(True, data)
    return response

def game(uuid=None):
    logger.info(f'Received game request with{"out id" if uuid is None else f" id {uuid}"}')
    if uuid:
        data = {
                'id': f'{uuid}',
                'board': 'dummyboard',
                'player1': 'batato',
                'player2': 'tomato'
                }
        response = Payload(success=True, message=f'Retrieved game for player ID {uuid}', data=data)
    else:
        data = {
                'id': 'Obina_melhor_que_etoo',
                'board': 'dummyboard',
                'player1': 'batato',
                'player2': 'tomato'
                }
        response = Payload(success=True, message='New game created', data=data)
    return response

def play(uuid, position):
    logger.info(f'Received request from player {uuid} to play on position {position}')
    data = {
            'id': f'{uuid}',
            'board': 'PLEIED',
            'player1': 'batato',
            'player2': 'tomato'
            }
    response = Payload(success=True, data=data)
    return response
