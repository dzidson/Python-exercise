import random

lower = "abcdefghijklmnoprstuvwxyz"
upper = "abcdefghijklmnoprstuvwxyz"
upper = str.upper(upper)

numbers = "123456789"
symbols = "[]{}()*;/.,_-"

all = lower + upper + numbers + symbols
lenght = 16


password = "".join(random.sample(all,lenght))

print(password)