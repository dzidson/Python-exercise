#wczytywanie plikow

nameandsurname = []

with open("imionanazwiska.txt" , "r", encoding="UTF-8") as file:
    for line in file:
        nameandsurname.append(tuple(line.replace("\n","").split(" ")))        #replace zamienia stare na nowe, split zmiana separatora


with open("imiona.txt" , "w", encoding="UTF-8") as file:
    for item in nameandsurname:
        file.write(item[0] + "\n") 

with open("nazwiska.txt" , "w", encoding="UTF-8") as file:
    for item in nameandsurname:
        try:
            file.write(item[1] + "\n")
        except IndexError:
            file.write("\n")
        
        """
        if (len(item)==2):                           inny sposób (nie profesionalny)
            file.write(item[1] + "\n")
        else:
            file.write("\n") 
        """