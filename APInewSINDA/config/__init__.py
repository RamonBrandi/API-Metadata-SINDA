def init_app(server):
    server.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    server.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///../db/SINDA-Metadados.db'