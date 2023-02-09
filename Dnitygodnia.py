#enumeration - spis - wyliczenie

from enum import IntEnum

Menu_Day = IntEnum('Menu_Day', {'Poniedzialek':1, 'Wtorek':2, 'Sroda':3, 'Czwartek':4, 'Piatek':5, 'Sobota':6, 'Niedziela':7})

#Przypisanie klucza do dnia (zamiast 1 -> Motto)
Day_Week = {
    Menu_Day.Poniedzialek : "Motto1",
    Menu_Day.Wtorek : "Motto2",
    Menu_Day.Sroda : "Motto3",
    Menu_Day.Czwartek : "Motto4",
    Menu_Day.Piatek : "Motto5",
    Menu_Day.Sobota : "Motto6",
    Menu_Day.Niedziela : "Motto7"
}

wybor = int(input("""Wybierz dzień tygodnia
1. Poniedziałek
2. Wtorek
3. Środa
4. Czwartek
5. Piątek
6. Sobota
7. Niedziela
"""))

print(Day_Week[wybor])
 