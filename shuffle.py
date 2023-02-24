#shuffle 

import random

#shuffle - tasowanie listy (zamiana kolejności)

cardlist = [
            'Ace', 'Ace', 'Ace', 'Ace',
            '2', '2', '2', '2',
            '3', '3', '3', '3',
            '4', '4', '4', '4',
            '5', '5', '5', '5',  
            '6', '6', '6', '6',
            '7', '7', '7', '7',
            '8', '8', '8', '8',
            '9', '9', '9', '9',
            '10', '10', '10', '10',
            'Jack', 'Jack', 'Jack', 'Jack',
            'Queen', 'Queen', 'Queen', 'Queen',
            'King', 'King', 'King', 'King',
            'Joker', 'Joker']


random.shuffle(cardlist)
print(cardlist)


