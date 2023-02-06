evenNumbersGenerator = (element
                        for element in range(20)
                        if (element % 2 == 0)
                        )

for item in evenNumbersGenerator:

    print(item)


#Generator - pozwala na generowanie, tworzenie, wyciąganie poszczególnych elementów na bieżąco.
