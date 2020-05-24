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
            "name": "Random",
            "position": [100.3308994, -20.4083342],
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
# for location in data["locations"]:
#    i, ratio = 0, 0
#    for i in range(len(locations)):
#        if (fuzz.ratio(locations[i][0], location["name"]) > ratio):
#            ratio = fuzz.ratio(locations[i][0], location["name"])
#            location["count"] = int(locations[i][1])

with open('data.json', 'w', encoding='utf8') as json_file:
    json.dump(data, json_file, ensure_ascii=False)

##############################################################################################

cp = cmd.run("git add data.json", check=True, shell=True)
print(cp)

message = f"last update : {data['lastUpdate']} "

cmd.check_output(['git', 'commit',  '-m', message])
cp = cmd.run("git push -u origin master -f", check=True, shell=True)
