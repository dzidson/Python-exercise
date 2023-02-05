#słownik


book = {1: "Ania z Zielonego wzgórza", 2: "Nielegalni", 3:"Imposible", 4:"SPY" }

print(book.get(4))   # pobieranie wartości ze slownika
book.update({5:"Imposible 2", 6:"Pies który jeździł koleją", 7:"Kubuś puchatek"}) # dodanie NAWET kilku kluczy i ich wartości do słownika
book[8] = "Kajakarstwo" # dodanie klucza i wartości
print(book)

del(book[3]) #usuwanie elementu
print(book)

book.popitem()
print(book)
print(len(book)) # sprawdzamy długość elementów 
