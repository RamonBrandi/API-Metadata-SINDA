from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_app(server):
    db.init_app(server)


