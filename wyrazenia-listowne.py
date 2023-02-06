liczby = [1, 2, 3, 4, 5, 6]

potegiDwojki = []
for element in liczby:
    potegiDwojki.append(element**2)

liczbyParzyste = []
for element in liczby:
    if (element % 2 == 0):
        liczbyParzyste.append(element)


potegiDwojki2 = [element**2
                 for element in range(20)
                ]
liczbyParzyste2 = [element
                  for element in liczby
                  if (element % 2 == 0)    
                  ]

"""
[co_zrobic_na_elemencie | for element in stara_lista | warunek_oparty_na_elemencie]
"""
