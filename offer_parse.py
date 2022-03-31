from bs4 import BeautifulSoup
import requests
import sqlite3
import sys

URL = "https://www.olx.pl/nieruchomosci/mieszkania/dolnoslaskie/q-sprzeda%C5%BC-mieszkania-dolno%C5%9Bl%C4%85skie/?search%5Bfilter_enum_rooms%5D%5B0%5D=one"

def parse_price(price):
    return float(price.replace(" ", "").replace("zł", "").replace(",","."))

db = sqlite3.connect("dane.db")
cursor = db.cursor()

if len(sys.argv) > 1 and sys.argv[1] == "setup":
    cursor.execute(''' CREATE TABLE offers (name TEXT, price REAL, city TEXT)''')
    quit()


page = requests.get(URL)
bs = BeautifulSoup(page.content, "html.parser")

for offer in bs.find_all("div", class_="offer-wrapper"):
    footer = offer.find("td", class_="bottom-cell")
    location = footer.find(
        "small", class_="breadcrumb").get_text().strip().split(",")[0]
    title = offer.find("strong").get_text().strip()
    price = parse_price(offer.find("p", class_="price").get_text().strip())

    cursor.execute("INSERT INTO offers VALUES (?, ?, ?)", (title, price, location))
    db.commit()
db.close()
