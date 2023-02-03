#wybór działania

wybor = int(input("1-dodawanie, 2-odejmowanie, 3-mnożenie, 4-dzielenie"))

a = int(input("Podaj pierwszą liczbę: " ))
b = int(input("Podaj drugą liczbę: " ))

if(wybor == 1):
    print("Wynik dodawania jest równy: ", a + b)
elif(wybor == 2):
    print("Wynik odejmowania jest równy: ", a - b)
elif(wybor == 3):
    print("Wynik mnożenie jest równy: ", a * b)
elif(wybor == 4):
    if(b == 0):
        print("Nie można dzielić przez zero")
    print("Wynik dzielenia jest równy: ", a / b)
       
else:
    print("Nie dokonałeś dobrego wyboru")