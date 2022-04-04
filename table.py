from sqlalchemy import Column, String, Integer, Float
from flask_sqlalchemy import SQLAlchemy
from flask import Flask


table = Flask(__name__)
table.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///BAZADANYCH.db"
db = SQLAlchemy(table)


class Hotele(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String)
    adress = Column(String)
    miasto = Column(String)
    latitiude = Column(Float)
    longitiude = Column(Float)
    place_id = Column(String)
    rating = Column(String)
    museum = Column(String)
    tourist_attraction = Column(String)
    cafe = Column(String)
    restaurant = Column(String)
    hotel = Column(String)


class Tourist_attractionWRO(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String)
    adress = Column(String)
    miasto = Column(String)
    latitiude = Column(Float)
    longitiude = Column(Float)
    place_id = Column(String)
    rating = Column(String)
    museum = Column(String)
    tourist_attraction = Column(String)
    cafe = Column(String)
    restaurant = Column(String)
    hotel = Column(String)


class Restaurant(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String)
    adress = Column(String)
    miasto = Column(String)
    latitiude = Column(Float)
    longitiude = Column(Float)
    place_id = Column(String)
    rating = Column(String)
    museum = Column(String)
    tourist_attraction = Column(String)
    cafe = Column(String)
    restaurant = Column(String)
    hotel = Column(String)

class Koncerty(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    place = db.Column(db.String)
    place_address = db.Column(db.String)
    city = db.Column(db.String)
    date = db.Column(db.String)
    start_time = db.Column(db.String)
    description = db.Column(db.String)
    link_image = db.Column(db.String)


class Spektakle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    place = db.Column(db.String)
    place_address = db.Column(db.String)
    city = db.Column(db.String)
    date = db.Column(db.String)
    start_time = db.Column(db.String)
    description = db.Column(db.String)
    link_image = db.Column(db.String)

class Kabarety(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    place = db.Column(db.String)
    place_address = db.Column(db.String)
    city = db.Column(db.String)
    date = db.Column(db.String)
    start_time = db.Column(db.String)
    description = db.Column(db.String)
    link_image = db.Column(db.String)
