from flask import Flask, request, Response, jsonify
import controller
import json
import ur
from loguru import logger

app = Flask(__name__)

@app.route('/game', methods=['GET'])
def game():
    logger.info('Received GET request on /game')
    if (uuid := request.args.get('id')):
        logger.info(f'Received ID {uuid}')
        return uuid
    else:
        logger.info('No ID provided, creating new game')
        return '01234567-89ab-cdef-0123-456789abcdef'

@app.route('/dice', methods=['GET'])
def dice():
    logger.info('Received GET request on /game')
    if not (uuid := request.args.get('id')):
        logger.info('ID not provided')
        return "Missing ID", 400
    else:
        logger.info(f'Received ID {uuid}')
        result = controller.dice(uuid)
        if result.success:
            logger.info('Received successful response')
            return jsonify({'success': result.success,
                'message': result.message,
                'data': result.data})
        else:
            logger.info('Request failed. Error: {result.message}')
            return f'Error: {result.message}', 500

@app.route('/play', methods=['POST'])
def play():
    logger.info(f'Received POST request on /play')
    return 'Ok'

