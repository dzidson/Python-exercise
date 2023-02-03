#listy

 
imiona = ["Arek", "Pawel", "Adrian", "Kuba"]
imiona.extend(["Michał,", "Łukasz"])
print(imiona)

imie = str.capitalize(input("Podaj imię: "))


if (imie) in imiona:
    print("Masz dostęp: ")
else:
    print("Nie masz dostępu")


