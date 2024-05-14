f = open("type-27/2022-early/B.txt")

n = int(f.readline())

a = [int(f.readline()) for i in range(n)]

s = [sum(a[0 : n // 2])]

# print(s)

for i in range(1, n):
    s.append(s[i - 1] - a[i - 1] + a[(i + n // 2 - 1) % n])

# print(f'{s=}')

summa = sum(a)

# print(f'{summa=}')

p = []
for i in range(n):
    p.append(summa - s[i])

# print(f'{p=}')

price = 0
for i in range(n // 2):
    price += i * a[i]
for i in range(n // 2, n):
    price += (n - i) * a[i]

# print(f'{price=}')

minim = price
min_k = 1
for i in range(1, n):
    price -= s[i]
    price += p[i]
    # print(f'{price=}, {minim=}')
    if price < minim:
        minim = price
        min_k = i + 1

print(min_k)