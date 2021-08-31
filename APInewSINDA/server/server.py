from flask import Flask
from APInewSINDA import config
from APInewSINDA import db
from APInewSINDA import migrate
from APInewSINDA import cli

def create_app():
    server = Flask(__name__)
    with server.app_context():
        config.init_app(server)
        db.init_app(server)
        migrate.init_app(server)
        cli.init_app(server)
        
    return server