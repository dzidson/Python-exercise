#cwiczenie gra


import random
from enum import Enum


def findAproximateValues(value):   #Losowa nagroda z przedziału (+-10%)
    lowervalues = value - 0.1 * value
    highervalues = value + 0.1 * value
    return random.randint(lowervalues, highervalues)

Event = Enum('Event', ['chest', 'empty'])

eventDictionary = {
                Event.chest: 0.6,
                Event.empty: 0.4
                }

eventList = tuple(eventDictionary.keys())
eventProbablity = tuple(eventDictionary.values())

Colour = Enum('Colour', {
                        'Green':'zielony',
                        'Orange':'Pomarańczowy',
                        'Purple':'Fiolletowy',
                        'Gold':'Złoty'
                        })

chestColourdictionary = {
                        Colour.Green: 0.75,
                        Colour.Orange: 0.2,
                        Colour.Purple: 0.04,
                        Colour.Gold: 0.01
                        }

chestColourList = tuple(chestColourdictionary.keys())
ChestColourProbablity = tuple(chestColourdictionary.values())

rewardChest = { 
                 chestColourList[reward]: (reward + 1) * (reward + 1) * 1000
                 for reward in range(len(chestColourList))
    }

game_Length = 5
gold_Acquired = 0
while game_Length > 0:
    game_Answer = input("Do you want to move forward?")
    if (game_Answer == 'yes'):
        print("Great, let's see what you got")
        drawEvent = random.choices(eventList, eventProbablity)[0]
        if (drawEvent == Event.chest):
            print("You have draw a chest")
            drawChest = random.choices(chestColourList, ChestColourProbablity)[0]
            print('The chest colour is', drawChest.value)
            game_Reward = findAproximateValues(rewardChest[drawChest])
            gold_Acquired = gold_Acquired + game_Reward
        elif(drawEvent == Event.empty):
            print("You have draw nothing, you are so unlucky")
    else:
        print("You can go just straigh, nothing else!")
        continue
    game_Length = game_Length - 1



print("Congratulation you collect", gold_Acquired , "gold")

