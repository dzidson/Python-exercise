#zagnieżdzone dane

lista = [
        {"Imie":"Arkadiusz", "wiek": "22", "Płeć": "Mężczyzna","numer telefonu": "666555222"},
        {"Imie":"Michał", "wiek": "22", "Płeć": "Mężczyzna","numer telefonu": "545678542"},
        {"Imie":"Andrzej", "wiek": "22", "Płeć": "Mężczyzna","numer telefonu": "564456456"},
        {"Imie":"Kuba", "wiek": "22", "Płeć": "Mężczyzna","numer telefonu": "123432344"}
        ]

lista1 = {
        "jkjksfsufduj": {'name':'John', 'sex':'Male', 'age':'27' },
        "ssdsaadaadqe": {'name':'Ana', 'sex':'Female', 'age':'27' },
        "sdadsasdasda": {'name':'Michał', 'sex':'Mele', 'age':'27' },
        "gjghjtyjfsga": {'name':'Nela', 'sex':'Female', 'age':'27' },
        "reyrttjzdgdz": {'name':'Amelia', 'sex':'Female', 'age':'27' }
}

lista2 = [
        "Arek",
        "Michał", 
        "Andrzej"
        ]

"""
for key in lista1:
        for secendkey in lista1[key]:
                print(secendkey, lista1[key][secendkey])
"""
for id, zawartosc in lista1.items():            # Uzywać tego jak jest słownik wewnatrz słownika 
        print("ID: ", id)
        for key in zawartosc:
                print(key, zawartosc[key])
