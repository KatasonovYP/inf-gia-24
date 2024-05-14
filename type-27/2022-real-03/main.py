f = open("type-27/2022-real-03/B.txt")
n, m = map(int, f.readline().split())
a = [(int(i) + 7) // 8 for i in f]

mx = 0
for i in range(n):
    s = 0
    for j in range(n):
        if abs(i - j) <= m:
            s += a[j]

    mx = max(mx, s)

print(mx)

s = mx = sum(a[: 2 * m + 1])
for i in range(m + 1, n - m):
    s = s - a[i - m - 1] + a[i + m]
    mx = max(mx, s)


print(mx)
