import os
from flask import Flask, request
from flask_cors import CORS

from .config import config_by_name

app = Flask(__name__)

@app.after_request
def add_cors_headers(response):
    # r = request.referrer[:-1]
    # response.headers.add('Access-Control-Allow-Origin', r)
    #response.headers['Access-Control-Allow-Origin'] = request.headers['Origin']
    response.headers['Access-Control-Allow-Credentials'] = 'true'
    response.headers.add('Access-Control-Allow-Headers', 'X-CSRF')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
    response.headers.add('Access-Control-Allow-Headers', 'Cache-Control')
    response.headers.add('Access-Control-Allow-Headers', 'X-Requested-With')
    response.headers.add('Access-Control-Allow-Headers', 'Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET, POST, OPTIONS, PUT, DELETE')

    return response

def create_app(config_name):

    app.config.from_object(config_by_name[config_name])

    # cors
    CORS(app, support_credentials=True)

    return app
