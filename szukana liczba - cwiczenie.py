szukanaLiczba = 40
x = 0

while x != szukanaLiczba:
    x = int(input("Podaj szukaną liczbę"))
    if (x > szukanaLiczba):
        print("Podana liczba jest za duża")
    elif (x < szukanaLiczba):
        print("Podana liczba jest za mała")
    else:
        print("UDAŁO SIE !")
    