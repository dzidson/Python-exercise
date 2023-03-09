#cat facts

import requests
import json
import pprint
import webbrowser
from enum import Enum

def modul():
    Menu = Enum('Menu', "cat dog")
    wybor = int(input("""Wybierz opcje: 
1. Kot
2. Pies
"""))

    animaltype = Menu(wybor).name
    ileCiekawostek = int(input("Ile ciekawostek chcesz wyświetlić?: "))


    paramsx = {
            "amount" : ileCiekawostek,
            "animal_type" : animaltype
        }

    r = requests.get("https://cat-fact.herokuapp.com/facts/random", paramsx)
    try:
            content = r.json()
    except json.decoder.JSONDecodeError:
            print("Niepoprawny format")
    else:
        if ileCiekawostek  == 1:
            print (content["text"])
                    
        else:
            for facts in content:
                print (facts["text"])
modul()