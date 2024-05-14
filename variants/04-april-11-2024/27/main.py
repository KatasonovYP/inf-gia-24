with open("./variants/04-april-11-2024/27/A.txt") as file:
    [gap, size, *data] = list(map(int, file.read().split("\n")[:-1]))

# max_sum = 0

# for i in range(0, len(data)):
#     if i % 100 == 0:
#         print(i)
#     for j in range(i + gap, len(data)):
#         for k in range(j + gap, len(data)):
#             max_sum = max(max_sum, data[i] + data[j] + data[k])

# print(max_sum)
first = 0
second = 0
summa = 0
for i in range(0, size - gap * 2):
    first = max(first, data[i])
    second = max(second, first + data[i + gap])
    third = data[i + gap * 2]
    summa = max(summa, second + third)
    # print(first, second, third)
print(summa)
