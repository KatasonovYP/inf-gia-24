'''no map'''

numbers = [1, 2, 3, 4, 5]
new_numbers = []
for num in numbers:
    squared = num ** 2
    subtracted = squared - 10
    new_numbers.append(subtracted)

print(new_numbers)
# [-9, -6, -1, 6, 15]

'''map realization'''
def my_map(func, iterable):
    result = []
    for item in iterable:
        result.append(func(item))
    return result


'''map apply'''
def process_number(num):
    squared = num ** 2
    subtracted = squared - 10
    return subtracted

numbers = [1, 2, 3, 4, 5]
new_numbers = my_map(process_number, numbers)


print(new_numbers)
# [-9, -6, -1, 6, 15]