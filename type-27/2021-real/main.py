f = open("type-27/2021-real/B.txt")
n = int(f.readline())
k = 89
r = {0: (0, 0)}
ms = 0
m = float("inf")

for _ in range(n):
    x = int(f.readline())
    t = {}
    for key in r:
        t[(key + x) % k] = (r[key][0] + x, r[key][1] + 1)
    if x % k not in t:
        t[x % k] = (x, 1)
    r = t.copy()
    if 0 in r:
        if ms < r[0][0]:
            ms = r[0][0]
            m = r[0][1]
        elif ms == r[0][0]:
            m = min(t[0][1], m)

print(m)
