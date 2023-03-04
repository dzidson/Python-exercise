import random

def wybor_liczb(ilosc, ile_wszystkich):
    print(random.sample(range(ile_wszystkich + 1), ilosc))

wybor_liczb(7,49)


'''  #CWICZENIE

listaliczbwylosowanych = []

def wybor_liczb(ilosc, ile_wszystkich):
    x = 0
    while x < ilosc:
        number = random.randint(ilosc, ile_wszystkich)
        if number not in listaliczbwylosowanych:
            listaliczbwylosowanych.append(number)
        else:
            continue
        x = x + 1

wybor_liczb(6, 49)
print(set(listaliczbwylosowanych))

'''