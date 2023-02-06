#wyrazenie zbioru


names = {'charls', 'adam', 'ania', 'Jola', 'arkadiusz'}

names = {
    name.capitalize()
    for name in names
    if name.startswith("c")
    }
print(names)