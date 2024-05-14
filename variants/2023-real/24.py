with open('variants/2023-real/data.txt') as file:
    data = file.readline()

letters = 'ABC'
last = 0
result = []

for i in range(len(data) - 1):
    if data[i] in letters and data[i + 1] in letters:
        result.append(data[last:i + 1])
        last = i + 1

print(max(list(map(len, result))))