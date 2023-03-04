#choice and choices


import random


film = ['film1', 'film2', ' film3', 'film4']

event = ['smierc', 'wygrana', 'utrata polowy zycia', 'przegrana', 'utrata zlota' ]

nagrodazeskrzynki = ['zielona', 'niebieska', 'filoetowa', 'pomaranczowa']

from collections import Counter

print(Counter(random.choices(nagrodazeskrzynki, [80, 0.05 , 0.005, 0.0005], k = 1000000)))