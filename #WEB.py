#WEB

import requests
import json
import pprint
import webbrowser

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
    questions = r.json()
except json.decoder.JSONDecodeError:
    print("Niepoprawny format")
else:
    for question in questions["items"]:
        pprint.pprint(question["link"]) 
        webbrowser.open_new_tab(question["link"])