alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

d = {}

for c in alpha:
    d[c] = 0

print(d)



with open('./24.txt') as file:
    for line in file:
        for i in range(len(line) - 1):
            if line[i] == 'A':
                d[line[i + 1]] += 1


print(d)
print(max(d.values()))