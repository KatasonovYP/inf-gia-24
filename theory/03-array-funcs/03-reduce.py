'''no reduce'''
numbers = [1, 2, 3, 4, 5]
result = 0
for num in numbers:
    result += num # *=

print(result)
# 15

'''reduce realization'''
def reduce(func, iterable, initial):
    acc = initial
    for item in iterable:
        acc = func(acc, item)
    return acc


'''filter apply'''
def add(x, y):
    return x + y

def multiply(x, y):
    return x * y

numbers = [1, 2, 3, 4, 5]
result = reduce(add, numbers, 0)
print(result)
# 15

result = reduce(multiply, numbers, 1)
print(result)
# 120