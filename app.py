from flask import Flask, request
import json
import ur
from loguru import logger

app = Flask(__name__)

@app.route('/')
def new_game():
    '''
    Looks for a new game to the player. First searches
    for games with only one player, if none is found,
    creates a new one. Returns the game ID and player ID.
    '''
    logger.info('Received request for new game')
    return 'Hello, World!'

@app.route('/<uuid:playerid>')
def get_status(playerid):
    logger.info(f'Received GET request for status of game containing player {playerid}')
    return 'Ok'

@app.route('/<uuid:playerid>', methods=['POST'])
def play(playerid):
    logger.info(f'Received POST request for status of game containing player {playerid}')
    return 'Ok'

@app.route('/<uuid:playerid>/throw', methods=['GET'])
def throw_dice(playerid):
    logger.info(f'Player {playerid} threw the dice')
    return ur.Game().throw_dice()
