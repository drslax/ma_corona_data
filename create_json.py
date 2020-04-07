import subprocess as cmd
import json
from fuzzywuzzy import fuzz
from scraper import Scraper

data = {
    "lastUpdate": "",
    "total": 0,
    "active": 0,
    "deaths": 0,
    "recovered": 0,
    "locations": [
        {
            "name": "Beni Mellal-Khénifra | جهة بني ملال خنيفرة",
            "position": [32.3308994, -6.4083342],
            "count": 0
        },
        {
            "name": "Casablanca-Settat | جهة الدار البيضاء سطات",
            "position": [33.5722677, -7.6572038],
            "count": 0
        },
        {
            "name": "Fès-Meknès | جهة فاس مكناس",
            "position": [34.0239579, -5.0368456],
            "count": 0
        },
        {
            "name": "Guelmim-Oued Noun | جهة كلميم واد نون",
            "position": [28.6480651, -10.7883981],
            "count": 0
        },
        {
            "name": "Marrakesh-Safi | جهة مراكش آسفي",
            "position": [31.7963265, -8.9873784],
            "count": 0
        },
        {
            "name": "Oriental | جهة الشرق",
            "position": [34.4048349, -2.9172135],
            "count": 0
        },
        {
            "name": "Rabat-Salé-Kénitra | جهة الرباط سلا القنيطرة",
            "position": [34.0806772, -6.7860605],
            "count": 0
        },
        {
            "name": "Souss-Massa | جهة سوس ماسة",
            "position": [30.0801613, -8.4726047],
            "count": 0
        },
        {
            "name": "Tangier-Tétouan-Al Hoceima | جهة طنجة تطوان الحسيمة",
            "position": [35.2169864, -5.5851266],
            "count": 0
        },
        {
            "name": "Drâa-Tafilalet | جهة درعة تافيلالت",
            "position": [30.9355212, -6.9501418],
            "count": 0
        },
        {
            "name": "Dakhla-Oued Ed Dahab | جهة الداخلة وادي الذهب",
            "position": [23.529232, -15.076926],
            "count": 0
        },
        {
            "name": "Laâyoune-Sakia El Hamra | جهة العيون الساقية الحمراء",
            "position": [27.159999, -12.234591],
            "count": 0
        }
    ]
}

scraped, locations = Scraper()
if scraped == None:
    exit
data["lastUpdate"], data["total"], data["deaths"], data["recovered"] = scraped[0], int(
    scraped[3]), int(scraped[2]), int(scraped[1])
data["active"] = data["total"] - data["deaths"] - data["recovered"]
data["lastUpdate"] = data["lastUpdate"].replace("H", ":")
data["lastUpdate"] = data["lastUpdate"][:6] + ' ' + data["lastUpdate"][6:]
print((data["lastUpdate"]))
for location in data["locations"]:
    i, ratio = 0, 0
    for i in range(len(locations)):
        if (fuzz.ratio(locations[i][0], location["name"]) > ratio):
            ratio = fuzz.ratio(locations[i][0], location["name"])
            location["count"] = int(locations[i][1])

with open('data.json', 'w', encoding='utf8') as json_file:
    json.dump(data, json_file, ensure_ascii=False)

##############################################################################################

cp = cmd.run("git add data.json", check=True, shell=True)
print(cp)

message = f"last update : {data['lastUpdate']} "

cmd.check_output(['git', 'commit',  '-m', message])
cp = cmd.run("git push -u origin master -f", check=True, shell=True)
