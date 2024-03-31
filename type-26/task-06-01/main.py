file = open('./data.txt')
data = file.read().split('\n')[1:]
data = [line.split() for line in data]
data = [[int(line[0]), int(line[1])] for line in data]
data.sort()

counter = 1
max_c = 0
max_r = 0

for it in range(0, len(data) - 1):
    if data[it][0] == data[it + 1][0]:
        if (data[it + 1][1] - data[it][1]) in (0, 1):
            counter += data[it + 1][1] - data[it][1]
        else:
            if counter > max_c:
                max_c = counter
                max_r = data[it][0]
            counter = 1

if counter > max_c:
    max_c = counter
    max_r = data[it][0]

print(max_c, max_r)