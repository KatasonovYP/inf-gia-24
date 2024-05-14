with open('variants/2024-early/A.txt') as file:
    data = list(map(int, file.read().split('\n')[1:-1]))

print(data)

mn = 10**10

for point in range(len(data)):
    current = []
    for i in range(len(data) // 2):
        # print(point, point + i, point - i)
        current += [data[(point + i) % len(data)] * i, data[point - i] * i]
    print(point, sum(current), current)
    mn = min(mn, sum(current))

print(f'{mn=}')