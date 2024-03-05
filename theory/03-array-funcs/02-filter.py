'''no filter'''
numbers = [2, 7, 1, 8, 4, 5]
result = []
for num in numbers:
    if num > 5:
        result.append(num)

print(result)
# [7, 8]

'''filter realization'''
def filter(func, iterable):
    result = []
    for item in iterable:
        if func(item):
            result.append(item)
    return result

'''filter apply'''
def greater_than_five(num):
    return num > 5

numbers = [2, 7, 1, 8, 4, 5]
result = filter(greater_than_five, numbers)

print(result)
# [7, 8]