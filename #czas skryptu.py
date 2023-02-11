#czas skryptu
import time


#cwiczenie dodawanie liczb
liczba = int(input("Podaj liczbe do której chcesz żeby zsumowało wszystkie liczby "))

def sumowanie(liczba):
    suma = 0
    for cyfra in range(1, liczba+1):
        suma = suma + cyfra
    return suma
  
def sumowanie2(liczba):
    return sum([liczba for liczba in range(1, liczba+1)])   #wyrażenie listowne

def sumowanie3(liczba):  #wzór na ciag artytmetyczny
    return (1 + liczba)/2*liczba



def funcion_perf(func, arg):
    start = time.perf_counter()
    func(arg)
    end = time.perf_counter()
    return end - start



print(funcion_perf(sumowanie, 15000000))

print(funcion_perf(sumowanie2, 15000000))

print(funcion_perf(sumowanie3, 15000))




"""
start = time.perf_counter()
print(sumowanie(liczba))
end = time.perf_counter()
print(end - start)

start = time.perf_counter()
print(sumowanie2(liczba))
end = time.perf_counter()
print(end - start)

start = time.perf_counter()
print(sumowanie3(liczba))
end = time.perf_counter()
print(end - start)
"""