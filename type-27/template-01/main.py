f = open("27_B.txt").read().split("\n")[1:]
data = [list(map(int, line.split())) for line in f]
m = []
summ = 0

for line in data:
    summ += max(line)

for it in data:
    it.sort()
    d1 = it[2] - it[0]
    if d1 % 109:
        print(it)
        m.append(it[2] - it[0])
    d2 = it[2] - it[1]
    if d2 % 109:
        print(it)
        m.append(it[2] - it[1])

if summ % 109:
    print(summ)
else:
    m.sort()
    print(m[:10])
    k = 0
    while (summ - m[k]) % 109 == 0:
        k += 1
    print(summ - m[k])
