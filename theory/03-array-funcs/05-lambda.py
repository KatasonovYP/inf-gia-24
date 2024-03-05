from functools import reduce

a = filter(lambda x: x > 5, [1, 6, 8, 2, 3])
print(tuple(a))

result = reduce(lambda a, b: a + b, [1, 2, 3], 0)

print(result)