def f(x, a):
    return ((x & 29 != 0) <= ((x & 17 == 0) <= (x & a != 0)))

limit = 1000

for a in range(0, limit):
    if all(f(x, a) for x in range(0, limit)):
        print(a)
        break