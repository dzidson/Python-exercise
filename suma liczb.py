
def suma(*arg):
    print(*arg)
    wynik = 0
    liczby = [*arg]
    for i in liczby:
        wynik = wynik + i
    return wynik

    
print("Suma liczb wynosi: ",suma(2, 24, 77, 754, 2342, 111))