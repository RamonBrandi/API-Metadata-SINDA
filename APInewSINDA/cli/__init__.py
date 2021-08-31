from sqlalchemy.engine.base import Engine
from APInewSINDA.db import db
import click

def init_app(server):

    @server.cli.command()
    def create_db():
        """Initialize the database"""
        db.create_all()