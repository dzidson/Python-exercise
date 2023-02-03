#dodaj 3 dodatnie liczby

i = 0
wynik = 0

print("Dodaj 3 parzyste liczby do siebie!")

while i < 3:
    x= int(input("Podaj liczbę do dodania: "))
    if( x % 2 == 0):
        wynik += x 
        print("Wynik obecnego dodawania to: ", wynik)
        i += 1
    else:
        print("Podana liczba jest nieparzysta. Podaj nową")
        continue