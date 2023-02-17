import time

def time_performence(func, *arg, how_many_time = 1):   #   *arg - argument wielowartosciowy 
    sum = 0 
    for i in range(0,how_many_time):
        start = time.perf_counter()
        func(*arg)
        end = time.perf_counter()
        sum = sum +(end - start)
    return sum

setContener = {i for i in range(1000)}
listContener = [i for i in range(1000)]

def in_element_in(what_value, contener):            #   poprawiona funkcja o nowy argument (żeby nie zmieniać "conteneru" w funkcji)
    if what_value in contener:
        return True
    else:
        return False

"""
def in_element_in(what_value):
    if what_value in setContener:
        return True
    else:
        return False
"""
print(time_performence(in_element_in, 450, setContener, how_many_time = 300))
print(time_performence(in_element_in, 450, listContener, how_many_time = 300))