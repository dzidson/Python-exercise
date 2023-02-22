#cwiczenie7

zadania = ['ugotuj obiad', 'zjedz obiad', 'umyj naczynia', 'idz na trening', 'przygotuj posilki na jutro']

for i, zadania in enumerate(zadania, 1):
    zadania = zadania.capitalize()
    print(i, zadania)
