"""

Wyrażenie słownikowe

"""

names = {'Charls', 'Adam', 'Ania', 'Jola', 'Arkadiusz'}
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
celcius ={'t1': 20, 't2': 8, 't3': 0, 't4': -5, 't5': -20}

namesLenght = {
    name : len(name)
    for name in names
    if name.startswith("A")
    }
print(namesLenght)

mnozoznko = {
    liczba : liczba*liczba
    for liczba in range(-20, 5)
}
print(mnozoznko)

farenhait = {
    key : celcius*1.8 + 32
    for key, celcius in celcius.items()
    if celcius > 5
    if celcius < 20
}
print(farenhait)
