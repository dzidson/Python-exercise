import requests

def check(url):
    try:
        r = requests.get(url)
        return r.status_code == 200
    except: 
        return False

def strony(nazwa_pliku):           #funkcja do pobierania stron z pliku
    with open(nazwa_pliku, "r") as file:
        web = file.readlines()
        web = [x.replace("\n", "") for x in web]
        return web

def filtrowanie(web):                #funkcja do filtrowania stron
    list_web = []
    for strona in web:
        if check(strona):
            list_web.append(strona)
    return list_web


def zapis(lista):      #funkcja do zapisywania stron
    with open('result.txt',"w") as file:
        for strona in true_websites:
            file.write(strona + "\n")


websites = strony('websites.txt')
true_websites = filtrowanie(websites)
print(true_websites)
zapis(true_websites)
