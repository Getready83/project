from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from flask import Flask
import sqlalchemy

db = Flask(__name__)
db.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///resta.db"
db = SQLAlchemy(db)

alembic = Alembic()
alembic.init_app(new)


class restauracje(base):

    __tablename__ = "restauracje"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    adress = Column(String)
    latitiude = Column(Float)
    longitiude = Column(Float)
    place_id = Column(String)
    rating = Column(String)


    def __init__(self, id, name, adress,latitiude,longitiude, place_id, rating):
        self.id = id
        self.name = name
        self.adress = adress
        self.latitiude = latitiude
        self.longitiude = longitiude
        self.place_id = place_id
        self.rating = rating



base.metadata.create_all(engine)
