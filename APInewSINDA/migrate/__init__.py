from flask_migrate import Migrate
from APInewSINDA import db
from APInewSINDA.model import models #noqa

migrate = Migrate()

def init_app(server):
    migrate.init_app(server, db)