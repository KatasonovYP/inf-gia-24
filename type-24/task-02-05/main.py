with open('./data.txt') as file:
    data = file.read().split('\n')[:-1]

counts = list(map(lambda x: x.count('G'), data))
mini = counts.index(min(counts))

d = dict.fromkeys('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 0)

for c in data[mini]:
    d[c] += 1

print(d)
print(max(d.values()))
