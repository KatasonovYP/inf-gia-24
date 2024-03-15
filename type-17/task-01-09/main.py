f = open('17.txt')
f = [int(i) for i in f]

max_sum = 0
count = 0

c = 0
summ = 0

for i in f:
    if i % 2 != 0:
        c += 1
        summ += i

sr = summ / c

for i in range(len(f) - 1):
    if  (f[i] % 5 == 0 or f[i + 1] % 5 == 0) and (f[i] < sr or f[i + 1] < sr):
        count += 1
        max_sum = max(max_sum, f[i] + f[i + 1])

print(count, max_sum)