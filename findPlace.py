import requests
import json
from sqlalchemy import Column, String, Integer, Float
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_alembic import Alembic
import sys


findPlace = Flask(__name__)
findPlace.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///BAZADANYCH.db"
db = SQLAlchemy(findPlace)

alembic = Alembic()
alembic.init_app(findPlace)


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

db.create_all()

with open("googleapi.txt")as f:
    apikey = f.read().strip()
APIKEY = apikey


"""
Warszawa
52.231777", "20.985670
52.248741", "21.006300
52.235204", "21.038041
52.217217", "21.006331
52.213277", "21.056981



Kraków
50.075951", "19.936347
50.049167", "19.938113
50.060949", "19.913058
50.060756", "19.957544



Wrocław
51.100494", "17.031409
51.111861", "17.012130
51.110580", "17.052827
51.122300", "17.034855"""
def findPlaces(loc=("52.231777", "20.985670"),radius=1500, pagetoken = None):
    lat, lng = loc
    type = "lodging"
    url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={lat},{lng}& &radius={radius}&type={type}&key={APIKEY}&{pagetoken}".format(lat=lat, lng=lng, radius=radius, type=type,APIKEY=APIKEY,pagetoken="&pagetoken="+pagetoken if pagetoken else "")

    print(url)
    response = requests.get(url)
    res = json.loads(response.text)
    print(res)
    print(res, len(res["results"]))

    for result in res["results"]:
        #adress = "" if not result["vicinity"] else ""
        #print(result["vicinity"])
        adr = result["vicinity"].split(",")
        """print(ad)
        ad1=ad[0]
        ad2=ad[1].replace(" ","")
        print(ad1)
        print(ad2)"""
        try:
            xx = Hotele(name=result["name"],
                    adress=adr[0],
                    miasto=adr[1].replace(" ", ""),
                    latitiude=result["geometry"]["location"]["lat"],
                    longitiude=result["geometry"]["location"]["lng"],
                    place_id=result["place_id"], rating=result.get("rating", 0),
                    museum="1" if "museum" in result["types"] else "0",
                    tourist_attraction="1" if "tourist_attraction" in result["types"] else "0",
                    cafe="1" if "cafe" in result["types"] else "0",
                    restaurant="1" if "restaurant" in result["types"] else "0",
                    hotel="1" if "lodging" in result["types"] else "0",
            )
            db.session.add(xx)
        except IndexError:
            pass
    db.session.commit()
        #info = ";".join(map(str,[result["name"],[result["vicinity"]],result["geometry"]["location"]["lat"],result["geometry"]["location"]["lng"],result.get("rating",0),result["place_id"]]))
        #print(info)
        #print(result["name"])
        #print(result["vicinity"])
        #print(result["types"])
        #print(result["geometry"]["location"]["lat"])
        #print(result["geometry"]["location"]["lng"])
        #print(result["place_id"])
        #print(result.get("rating", 0))
        #print(str(result["photos"]["html_attributions"]))
        #print(str(result["photos"]["photo_reference"]))

    pagetoken = res.get("next_page_token", None)

    print("here -->> ", pagetoken)
    db.session.commit()
    return pagetoken

# pagetoken = "CpQFhwIAADQWOcVI1wll-B869Z24El48rXw18gKoab_keD65V18zFEvPjKIfrS79Pc_vXJcZQtOuF0RObQG20ph-GE3ssP3k1fu8zsYbw5g3UPbSjAvQLdXkdD1qAWztXj7hc5Kxc4pYRyGM1_ljVOHg3Py_zSlYscnoNjCvRua2MDQgusCsEquNqGREFdvhjDkbeMhEFYxHucTnIn96OxIJEpamePTHsBooYyPBaa_ejGZ_C99QeDjpSkSKBgEe3aL1uWKlYhsGKh7biQUR5rKsKPodwccLIrW8Gr5tag3NH0sLPExHHvqzlpkj--KIuydTVjPH7u2zHxmPByServ2S5xjXYUBRr-ly3e1xPsVMhZZH9TxfttCIHLscBvpvCswIfaGYdl3bEzsrFISfpp0rpKtlp9gWGY7Tbk2n6s3etCHQEHn2qmM8bsJwkZV81pUWN0j9C9RX-ywOyIKY2yp1w_Iq1mRwOwY4mckbicOoooHiV6JER4xe7Kizw9hbXOnezn_NMk15TLwRoXlfL1s73uwogo-VWE8c-V1HqRpWQSyudRhLwhOEclrICXIdxICOgTgYO1z57xCEerw3QUL_7MPDrlbbh_AlX8I6Jfe8IhQ1Fkqu_njatm6aBTjkp2CSqlvZJpI_Lrv330VcyFEqBkGn7NJew3I9xofSrBaXFa8ABi6DXQm6-yC32OEyf7GHNXINjT1IB0yh6KR6c0qzaqiqOzKcuuai9XqEMQNNKyi6EuhzH5TP9YA56N3JhnXRFhs2aWHZhLlieVI6_uqzpZSgYjUem8aQrMTlmHw0kIYU8I-Ca041C4Zm2gMezwygRrhzsOoAmbmu96nft0KuIWTB3A_xGVKYQ2qjb2KRM7nsglnSEhDoNs8EhvuIm0FQs30YSCp5GhRO3b3Tn5rsLuwiWgu8hwEGhL0S1A"
pagetoken = None

while True:
    pagetoken = findPlaces(pagetoken=pagetoken)
    import time
    time.sleep(5)

    if not pagetoken:
        break

