#APIKEY

import requests
import json
import pprint
import webbrowser

params = {
    "api_key" : "91af533620d24932987f6735003aa68e",
    "country" : "PL",
    "year" : "2022",
    "month" : "01",
    "day" : "01",
    "language" : "PL"
}

r = requests.get("https://holidays.abstractapi.com/v1/", params)


try:
    content = r.json()
except json.decoder.JSONDecodeError:
    print("Niepoprawny format")
else:
    print(content)
    print(r.status_code)
