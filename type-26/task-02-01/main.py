from math import ceil
from functools import reduce

with open("26.txt") as file:
    data = list(map(int, file.read().split("\n")[1:-1]))

data.sort()
sm = sum(filter(lambda x: x <= 50, data))
data = list(filter(lambda x: x > 50, data))

center = len(data) // 2
part_1 = data[:center]
part_2 = data[center:]

# for it in part_1:
#     sm += it * 0.75

sm += reduce(lambda a, b: a + b * 0.75, part_1, 0)
sm += sum(part_2)

print(ceil(sm), data[len(data) // 2 - 1])
