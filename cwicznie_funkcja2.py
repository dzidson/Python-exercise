def sum_positives(numbers):
    return max([number for number in numbers if number > 0])
 
numbers = [1, -2, 3, 0, -4, 5]
print(sum_positives(numbers)) 