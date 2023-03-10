#API
import requests
import json
import pprint

params = {
        'site' : "stackoverflow",
        'sort' : "votes",
        'order' : "desc",
        'fromdate' : '2023-02-01',
        'tagged' : 'python',
        'min' : "15"
        }

r = requests.get("https://api.stackexchange.com/2.2/questions/", params)

try:
    tasks = r.json()
except json.decoder.JSONDecodeError:
    print("Niepoprawny format")
else:
    pprint.pprint(tasks) 
    