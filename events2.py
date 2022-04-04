import requests
import re
import json

URL = "https://www.kupbilecik.pl/kabarety/?q=&qt=kabaret&qw=W&qs=&qo=ASC&qn=1"


response = requests.get(URL)
lines = response.text
with open("koncerty.txt", "w", encoding="utf-8") as f:
    f.write(lines)
"""
with open("kabarety.txt", "r", encoding="utf-8") as f:
    lines = f.read()"""

data_str = re.findall("<script type=\"application/ld\\+json\">(.+)</script>.+<script type=\"text/javascript\">", lines, re.DOTALL)[0].strip()
data_json = json.loads(data_str)
print(data_json)

"""
print(data_json[0]["@type"])
print(data_json[0]["name"])
print(data_json[0]["startDate"][:10])
print(data_json[0]["startDate"][11:16])
nazwa_miejsca = [data_json[0]["location"]["@type"], data_json[0]["location"]["name"]]
address= data_json[0]["location"]["name"]
print(data_json[0]["location"]["address"]["streetAddress"])
print(data_json[0]["location"]["address"]["addressLocality"])
print(data_json[0]["location"]["address"]["addressRegion"])
print(data_json[0]["description"])
print(data_json[0]["image"])

nazwa_miejsca = ": ".join(name1)
address = ", ".join([data_json[0]["location"]["address"]["streetAddress"],data_json[0]["location"]["address"]["addressLocality"],data_json[0]["location"]["address"]["addressRegion"]])

print("*"*40)
print(nazwa_miejsca)
print(address)"""