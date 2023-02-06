definicje = {}    #defniniuje pusty słownik


while(True):

    print("1 - Dodaj definicje")
    print("2 - Znajdź definicje")
    print("3 - Usuń definicje")
    print("4 - Zakończ program")

    wybor = input("Co chcesz zrobić ?")


    if (wybor == "1"):
        key = input("Podaj słowo które chcesz zdefiniować: ")
        definicja = input("Podaj definicje: ")
        definicje[key] = definicja
        print("Definicja dodana pomyślnie!")
    elif (wybor == "2"):
        key = input("Podaj słowo ktorego chcesz definicje: ")
        if key in definicje:
            print(definicje[key])
        else:
            print("Nie ma takiej definicji")
    elif (wybor == "3"):
        key = input("Podaj defincje do usuniecia: ")
        if key in definicje:
            del definicje[key]
            print("Usunięto definicje o nazwie", key)
        else:
            print("Nie ma takiej definicji o nazwie: ", key)
    elif (wybor == "4"):
        print("Zakończono program")
        break
    else:
        print("Wybierz co chcesz zrobić!")
    


