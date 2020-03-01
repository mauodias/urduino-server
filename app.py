from flask import Flask, request
import json
import ur
from loguru import logger

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/play', methods=['POST'])
def play():
    logger.info(f'{request.json}')

@app.route('/draw', methods=['GET'])
def draw():
    return ur.draw()
