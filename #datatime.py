#datatime

import requests
import json
import pprint
import webbrowser
from datetime import datetime,timedelta

print(datetime.today())

timeBefore = timedelta(days=20)
searchDate = datetime.today() - timeBefore
print(searchDate)
print(int(searchDate.timestamp()))



params = {
        'site' : "stackoverflow",
        'sort' : "votes",
        'order' : "desc",
        'fromdate': int(searchDate.timestamp()),
        'tagged' : 'python',
        'min' : "15"
        }

r = requests.get("https://api.stackexchange.com/2.2/questions/", params)

try:
    questions = r.json()
except json.decoder.JSONDecodeError:
    print("Niepoprawny format")
else:
    for question in questions["items"]:
        webbrowser.open_new_tab(question["link"])