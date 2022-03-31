import re
import json
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
"""URL = "https://www.kupbilecik.pl/koncerty/?q=&qt=muzyka&qw=D&qs=&qo=ASC&qn=1"""

koncerty = Flask(__name__)
koncerty.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///Malopolskie.db"
db = SQLAlchemy(koncerty)

class Koncerty(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    place = db.Column(db.String)
    place_address = db.Column(db.String)
    date = db.Column(db.String)
    start_time = db.Column(db.String)
    description = db.Column(db.String)
    link_image = db.Column(db.String)

db.create_all()

"""response = requests.get(URL)
lines = response.text"""

with open("koncerty.txt", "r", encoding="utf-8") as f:
    lines = f.read()

data_str = re.findall("<script type=\"application/ld\\+json\">(.+)</script>.+<script type=\"text/javascript\">", lines, re.DOTALL)[0].strip()
data_json = json.loads(data_str)



for data_json in data_json:
    try:
        print(data_json["location"]["name"])
        nazwa_miejsca = [data_json["location"]["@type"],data_json["location"]["name"]]
        nazwa_miejsca = ": ".join(nazwa_miejsca)
        print(nazwa_miejsca)
        address = ", ".join([data_json["location"]["address"]["streetAddress"],
                             data_json["location"]["address"]["addressLocality"],
                             data_json["location"]["address"]["addressRegion"]])

        konc = Koncerty(name=data_json["name"],place=data_json["location"]["name"],
                    place_address=address,date=data_json["startDate"][:10],
                    start_time=data_json["startDate"][11:16],
                    description=data_json["description"],
                    link_image=data_json["image"])
        db.session.add(konc)
    except KeyError:
        pass

db.session.commit()

"""print(data_json[0]["@type"])
print(data_json[0]["name"])
print(data_json[0]["startDate"][:10])
print(data_json[0]["startDate"][11:16])
address= data_json[0]["location"]["name"]
print(data_json[0]["location"]["address"]["streetAddress"])
print(data_json[0]["location"]["address"]["addressLocality"])
print(data_json[0]["location"]["address"]["addressRegion"])
print(data_json[0]["description"])
print(data_json[0]["image"])
print(data_json[0]["@type"])
nazwa_miejsca = ": ".join(nazwa_miejsca)
#address = ", ".join([data_json[0]["location"]["address"]["streetAddress"],data_json[0]["location"]["address"]["addressLocality"],data_json[0]["location"]["address"]["addressRegion"]])

print("*"*40)
print(nazwa_miejsca)
print(address)"""