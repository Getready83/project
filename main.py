from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_alembic import Alembic
from table import Hotele, Tourist_attractionWRO, Restaurant, Koncerty, Spektakle, Kabarety


main = Flask(__name__)
main.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///BAZADANYCH.db"
db = SQLAlchemy(main)

alembic = Alembic()
alembic.init_app(main)


class Tourist:
    def __init__(self):
        self.choice = []
        self.place = []
        self.time = []
        self.todo = []



class Enterteiment:
    def __init__(self, request):
        self.choice = []
        self.place = []
        self.time = []
        self.todo = []
        self.koncerty = []
        self.spektakle = []
        self.kabarety = []
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
        return self.koncerty, self.spektakle, self.kabarety, self.events

    def koncert(self):
        self.koncerty = []
        for event in db.session.query(Koncerty).all():
            #c = [i for i in enterteiment_type if i in self.todo[0]]
            if "koncert" in self.todo[0]:
                if self.date in event.date:
                    if self.city in event.city:
                        self.koncerty.append(event)
                    elif not self.city:
                        self.koncerty.append(event)


    def spektakl(self):
        for event in db.session.query(Spektakle).all():
            self.spektakle.append(event)
            #c = [i for i in enterteiment_type if i in self.todo[0]]
            if "spektakl" in self.todo[0]:
                if self.date in event.date:
                    if self.city in event.city:
                        print(event.name, event.date)
                    elif not self.city:
                        print(event.name, event.date)
            return self.spektakle

    def kabaret(self):
        for event in db.session.query(Kabarety).all():
            self.kabarety.append(event)
            #c = [i for i in enterteiment_type if i in self.todo[0]]
            if "kabaret" in self.todo[0]:
                if self.date in event.date:
                    if self.city in event.city:
                        print(event.name, event.date)
                    elif not self.city:
                        print(event.name, event.date)
            return self.kabarety

    def anywhere(self):
        if "Anywhere" == self.city:
            if "koncert" in self.todo[0]:
                for event in db.session.query(Koncerty).all():
                    self.events.append(event)
                    if self.date in event.date:
                        print(event.name, event.city, event.place_address)
            if "spektakl" in self.todo[0]:
                for event in db.session.query(Spektakle).all():
                    self.events.append(event)
                    if self.date in event.date:
                        print(event.name, event.city, event.place_address)
            if "kabaret" in self.todo[0]:
                for event in db.session.query(Kabarety).all():
                    self.events.append(event)
                    if self.date in event.date:
                        print(event.name, event.city, event.place_address)
            return self.events

    def wheresleep(self):
        for place in db.session.query(Hotele).all():
            if self.city in place.miasto:
                if place.rating =="4.8":
                    print(f"Warto się zatrzymać {place.name}przy ulicy: {place.adress}")








#enterteiment_type = ["koncert", "spektakl", "kabaret"]


"""
x = ["pojechac na kabaret"]
print(x,"x")
a = x[0]
print(a,"a")
c=a.split(",")
print(c,"c")
b=a.replace(" ", ",")

print(b)



lista = ["koncert", "wrocław", "123"]
if "koncert" in lista:
    print("jest")

for event in db.session.query(Koncerty).filter(
        Koncerty.city == "Wrocław").all():
    print(event.name, event.date, event.city)"""


"""wroclaw = []

for place in db.session.query(Tourist_attractionWRO).filter(Tourist_attractionWRO.miasto=="Wrocław").all():
    if place.museum == "1":
        if place.rating == "4.5":
            wroclaw.append(place.name)
print(wroclaw[1:3])
for place in wroclaw:
    print(place[1:4])"""

"""for event in db.session.query(Spektakle).filter(Spektakle.city=="Wrocław").all():
    print(event.date)
"""