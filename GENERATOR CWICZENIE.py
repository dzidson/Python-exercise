#GENERATOR CWICZENIE

generator = (
    liczba
    for liczba in range(100, 471)
    if liczba % 7 == 0
    if liczba % 5 != 0    
    )

for liczba in generator:
    print(liczba)


