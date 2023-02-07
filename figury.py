import math

def pole_kwadratu(a):
    return a * a

def pole_prostokata(a, b):
    return a * b

def pole_kola(r):
    return math.pi * r ** 2

def pole_trojkata(a, h):
    return 0.5 * a * h

def pole_trapezu(a, b, h):
    return (a + b) / 2 * h
    
while(True):

    wybor = int(input("1 - pole kwadratu, 2 - pole prostokąta, 3 - pole koła, 4 - pole trójkąta, 5 - pole trapezu, 6 - przerwij program "))

    if(wybor == 1):
        a = int(input("Podaj długość boku: " ))
        pole_kwadratu(a)
        print("Pole powierzchni kwadratu o bokach ", a , " wynosi: ", pole_kwadratu(a))

    elif(wybor == 2):
        a = int(input("Podaj długość pierwszego boku: " ))
        b = int(input("Podaj długość drugiego boku: " ))  
        print("Pole powierzchni kwadratu o bokach ", a, " i ", b , " wynosi: ", pole_prostokata(a, b))

    elif(wybor == 3):
        r = int(input("Podaj promień: " ))
        print("Pole powierzchni koła o promieniu ", r , " wynosi: ", pole_kola(r))

    elif(wybor == 4):
        a = int(input("Podaj podstawę trójkąta: " ))
        h = int(input("Podaj wysokość trójkąta: " ))
        print("Pole powierzchni trójkąta o długości podstawy ", a ," i wsyokości ", h,  " wynosi: ", pole_trojkata(a, h))

    elif(wybor == 5):
        a = int(input("Podaj długość podstawy górnej: " ))
        b = int(input("Podaj długość podstawy dolnej: " ))
        h = int(input("Podaj wysokość: " ))
        print("Pole powierzchni trapezu o długości podstaw ", a, " i ", b , " oraz wysokości ", h,  " wynosi: ", pole_trapezu(a, b, h))
    elif(wybor == 6):
        print("Do widzenia!")
        break
    else:
        print("Nie wybrałeś nic!")
    