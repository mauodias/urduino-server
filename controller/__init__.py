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
        pass
    else:
        pass
