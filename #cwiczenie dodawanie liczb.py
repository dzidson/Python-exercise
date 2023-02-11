#cwiczenie dodawanie liczb



liczba = int(input("Podaj liczbe do której chcesz żeby zsumowało wszystkie liczby "))

"""
def sumowanie(liczba):
    suma = 0
    for cyfra in range(1, liczba+1):
        suma = suma + cyfra
    return suma

print(sumowanie(5))  
"""

def sumowanie2(liczba):
    return sum([liczba for liczba in range(1, liczba+1)])   #wyrażenie listowne

print(sumowanie2(liczba))


def sumowanie3(liczba):  #wzór na ciag artytmetyczny
    return (1 + liczba)/2*liczba

print(sumowanie3(liczba))


