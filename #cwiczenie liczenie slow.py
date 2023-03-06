#cwiczenie liczenie slow


sciezka = "tekst.txt"
slowo = "Kot"

with open(sciezka, 'w', encoding="UTF-8") as file:
    file.write('Kot jest dumnym zwierzęciem \n')

try:
    with open(sciezka, 'r', encoding="UTF-8") as file:
        tekst = file.read()
        ilosc = tekst.count(slowo)
        print(f"Liczba wystąpień '{slowo}' w pliku {sciezka} to {ilosc}.")
except FileNotFoundError:
    print(f"Plik o ścieżce {sciezka} nie został znaleziony.")
except PermissionError:
    print(f"Brak uprawnień do odczytu pliku {sciezka}.")
