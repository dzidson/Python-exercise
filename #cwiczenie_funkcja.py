#cwiczenie_funkcja



def sumowanie(lista):
    suma = 0 
    for liczba in lista:
        if liczba > 0:
            suma += liczba
    return suma

lista = [2, 3, 4, 5, -6, 6, 7, -8, 6, 7, 8, -2, 1, 2, -4]
print("Suma wszystkich liczb większych od 0 w liście = ", sumowanie(lista))