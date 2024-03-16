with open('26.txt') as file:
    budget = int(file.readline().split()[1])
    data = file.read().split('\n')[:-1]
    data = [line.strip().split() for line in data]
    data = [[int(line[0]), int(line[1]), line[2]] for line in data]
    type_a = []
    type_b = []
    for it in data:
        if it[2] == 'A':
            type_a.append(it[0] * it[1])
        else:
            type_b.append(it[:2])

sm = sum(type_a)
type_b.sort(key=lambda x: x[0])
count_b = 0
remain = budget - sm

for it in type_b:
    for j in range(it[1]):
        if remain - it[0] >= 0:
            remain -= it[0]
            count_b += 1

print(count_b, remain)
print(5895, 227)
