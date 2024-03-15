f = open("17.txt")
f = [abs(int(i)) for i in f]


maxi = f[0]
max_sum = f[0]
count = 0

for x in f:
    if x % 10 == 3:
        maxi = max(maxi, x)

print(maxi)

for i in range(len(f) - 1):
    if (f[i] % 10 == 3) != (f[i + 1] % 10 == 3):
        sm = f[i] ** 2 + f[i + 1] ** 2
        if sm >= maxi ** 2:
            count += 1
            max_sum = max(max_sum, sm)

print(count, max_sum)
