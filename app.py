# top 5 miast imprez kabaretowych( w okreslonym terminie)
# jade do miasta i co moge zobaczyć ( imprezy koncerty muzea w danym terminie)
from flask_sqlalchemy import SQLAlchemy
from flask_alembic import Alembic
from main import Enterteiment
from table import Hotele, Tourist_attractionWRO, Restaurant, Koncerty, Spektakle
import requests
from flask import Flask, render_template, redirect, request


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///BAZADANYCH.db"
db = SQLAlchemy(app)

alembic = Alembic()
alembic.init_app(app)

@app.route("/", methods=["GET", "POST"])
def formularz():
    #obj = Enterteiment(request)
    city = request.form.get("city")
    date = request.form.get("date")
    info = request.form.get("info")
    if request.method == "POST":
        obj.execute()
        print(city)
        print(date)
        print(info)
        return redirect("/result/")
    return render_template("formularz.html",
                    city=city,
                    date=date,
                    info=info
    )

"""@app.route("/", methods=["POST"])
def formularzPOST():
    city = request.form.get("city", "")
    date = request.form.get("date", "")
    info = request.form.get("info", "")
    return redirect("/result/")"""


@app.route("/result/", methods=["GET", "POST"])
def result():
    obj = Enterteiment(request)
    city = request.form.get("city")
    date = request.form.get("date")
    info = request.form.get("info")
    if request.method == "POST":
        obj.execute()

    return render_template("result.html", enterteiment=obj)


app.run(debug=True)
