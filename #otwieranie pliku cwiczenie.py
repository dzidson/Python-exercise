#otwieranie pliku cwiczenie


def wczytanie_pliku(plik):
    try:
        with open(plik, "r", encoding="UTF-8") as file:
            return file.read()
    except FileNotFoundError:
        print("Nie odnaleziono pliku, podaj dokładną ścieżkę")


nazwa_pliku = input("Podaj nazwe pliku do wczytania: \n")

wczytany_plik = wczytanie_pliku(nazwa_pliku)
print(wczytany_plik)