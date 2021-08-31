from sqlalchemy import Column, String
from APInewSINDA.db import db


class Pcd(db.Model):
    __tablename__ = 'pcd'
    id = db.Column("id", db.Integer, primary_key=True)
    city = db.Column("Municipio", String)
    state = db.Column("estado", String)
    zone = db.Column("Regiao", String)
    latitude = db.Column("latitude", String)
    longitude = db.Column("longitude", String)
    data_inicial = db.Column("Data Inicial", String)
    data_final = db.Column("Data Final", String)
    
    def __repr__(self):
        return self.city
    
class Buoy(db.Model):
    __tablename__ = 'boias'
    id = db.Column("nome", String, primary_key=True)
    data_inicial = db.Column("Data Inicial", String)
    data_final = db.Column("Data Final", String)
    latitude = db.Column("latitude", String)
    longitude = db.Column("longitude", String)
    
    def __repr__(self):
        return self.id



