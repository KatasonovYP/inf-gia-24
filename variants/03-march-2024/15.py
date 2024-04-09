n = -1000
m = 1000


def f(x, y, a):
    return ((x in a) <= (x**2 <= 81)) and ((x**2 <= 36) <= (x in a))


a = set([i for i in range(n, m)])

for x in range(n, m):
    for y in range(n, m):
        if not f(x, a):
            a.remove(x)
print(sorted(list(a)), len(a) - 1)
