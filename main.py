from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_alembic import Alembic
from table import Hotele, Tourist_attractionWRO, Restaurant, Koncerty, Spektakle, Kabarety
import random


main = Flask(__name__)
main.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///BAZADANYCH.db"
db = SQLAlchemy(main)

alembic = Alembic()
alembic.init_app(main)


class Tourist:
    def __init__(self, request):
        self.choice = []
        self.place = []
        self.time = []
        self.todo = []
        self.request = request
        self.sigthsees = []
        self.restaurants =[]

    def takeChoice(self):
        self.city = self.request.form.get("city", "")
        self.place.append(self.city)
        self.date = self.request.form.get("date", "")
        self.time.append(self.date)
        self.to_do = self.request.form.get("info", "")
        self.todo.append(self.to_do)
        return self.city, self.date, self.todo

    def sigthsee(self):
        self.sigthsees = []
        self.restaurants = []
        for travel in db.session.query(Tourist_attractionWRO).all():
            if "zwiedzanie" in self.todo[0]:
                if self.city in travel.miasto and travel.tourist_attraction == "1" and travel.rating == "4.9":
                    print(travel.name, travel.adress,travel.miasto)
                    self.sigthsees.append(travel)
                return self.sigthsees

        for travel in db.session.query(Restaurant).all():
            if "restauraja" in self.todo[0]:
                if self.city in travel.miasto and travel.restaurant == "1" and travel.rating == "4.9":
                    self.restaurants.append(travel)
                    print(travel.name, travel.adress, travel.miasto)


    def execute(self):
        self.takeChoice()
        self.sigthsee()
        return self.sigthsees, self.restaurants



class Enterteiment:
    def __init__(self, request):
        self.choice = []
        self.place = []
        self.time = []
        self.todo = []
        self.koncerty = []
        self.spektakle = []
        self.kabarety = []
        self.hotele = []
        self.events = []
        self.request = request


    def takeChoice(self):
        self.city = self.request.form.get("city", "")
        self.place.append(self.city)
        self.date = self.request.form.get("date", "")
        self.time.append(self.date)
        self.to_do = self.request.form.get("info", "")
        self.todo.append(self.to_do)
        return self.city, self.date, self.todo

    def execute(self):
        self.takeChoice()
        self.koncert()
        self.spektakl()
        self.kabaret()
        self.anywhere()
        self.wheresleep()
        return self.koncerty, self.spektakle, self.kabarety, self.events, self.hotele

    def koncert(self):
        self.koncerty = []
        tourists = ["koncert", "Koncert", "koncerty", "Koncerty"]
        for tourist in tourists:
            if tourist in self.todo[0]:
                for event in db.session.query(Koncerty).all():
                    if self.date in event.date and self.city in event.city:
                        self.koncerty.append(event)
                    """ if self.city in event.city:
                        self.koncerty.append(event)
                    elif not self.city:
                        self.koncerty.append(event)"""
        return self.koncerty

    def spektakl(self):
        self.spektakle = []
        for event in db.session.query(Spektakle).all():
            #c = [i for i in enterteiment_type if i in self.todo[0]]
            if "spektakl" in self.todo[0]:
                if self.date in event.date and self.city in event.city:
                    self.spektakle.append(event)
                    """if self.city in event.city:
                        print(event.name, event.date)
                    elif not self.city:
                        print(event.name, event.date)"""
        return self.spektakle

    def kabaret(self):
        for event in db.session.query(Kabarety).all():
            #c = [i for i in enterteiment_type if i in self.todo[0]]
            if "kabaret" in self.todo[0]:
                if self.date in event.date and self.city in event.city:
                    self.kabarety.append(event)
                    """self.kabarety.append(event)
                        print(event.name, event.date)
                    elif not self.city:
                        print(event.name, event.date)"""
        return self.kabarety

    def anywhere(self):
        self.events = []
        if "Anywhere" == self.city:
            if "koncert" in self.todo[0]:
                for event in db.session.query(Koncerty).all():
                    if self.date in event.date:
                        self.events.append(event)
            if "spektakl" in self.todo[0]:
                for event in db.session.query(Spektakle).all():
                    if self.date in event.date:
                        self.events.append(event)
            if "kabaret" in self.todo[0]:
                for event in db.session.query(Kabarety).all():
                    if self.date in event.date:
                        self.events.append(event)
            return self.events

    def wheresleep(self):
        self.hotele = []
        for place in db.session.query(Hotele).all():
            if self.city in place.miasto and place.rating =="4.8":
                self.hotele.append(place)
        #print(random.choice(self.hotele))
        return self.hotele
                    #print(f"Warto się zatrzymać {place.name}przy ulicy: {place.adress}")

"""obj = Enterteiment(request)
obj.execute()"""

"""obj = Tourist(request)
obj.execute()"""
