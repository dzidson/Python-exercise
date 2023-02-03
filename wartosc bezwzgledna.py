#WARTOŚĆ BEZWZGLĘDNA

#Zrobione na 2 sposoby :)

import math

x = int(input("Podaj pierwszą liczbę z której chcesz zrobić wartość bezwzględną"))
y = int(input("Podaj drugą liczbę z której chcesz zrobić wartość bezwzględną"))
print("Wartość bezwzględna z", x, "jest równa: ", math.fabs(x))

if(y < 0):
    print("Wartość bezwzględna z", y, "jest równa: ", (y*(-1)))
else:
    print("Wartość bezwzględna z", y, "jest równa: ", y)



