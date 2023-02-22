import random

def will_weapon_hit(weaponChance):              # stworzenie funckji czy broń trafi
    IsHitChance = random.uniform(0,100)             # losowanie liczby od 0 do 100 
    if (IsHitChance < weaponChance):
        return "hit"
    else:
        return "no hit"

listHit = []   #stworzenie listy w której zapisują sie wyniki 

x = 0
while x < 100:
    x = x + 1
    listHit.append(will_weapon_hit(50))

from collections import Counter 
dictionaryHit = Counter(listHit)
print(dictionaryHit)


