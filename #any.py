#any - funkcja ANY sprawdza, czy JAKAKOLWIEK wartość to TRUE


number1 = [1, 3, 5, 6, 7, 9]
number2 = [1, 3, 5, 7, 9, 11]

'''
def any_even_parzysta(lista):
    for i in lista:
        if i % 2 == 0:
             return True 
    return False
'''

def any_even_parzysta(lista):
    return any(i % 2 == 0 for i in lista)

print(any_even_parzysta(number1))
print(any_even_parzysta(number2))