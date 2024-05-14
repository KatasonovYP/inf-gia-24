with open('26.txt') as file:
    data = list(map(int, file.read().split('\n')[1:-1]))

data.sort(reverse=True)

selected = [data[0]]

for pie in data[1:]:
    if selected[-1] - pie >= 8:
        selected.append(pie)


print(len(selected), selected[-1])