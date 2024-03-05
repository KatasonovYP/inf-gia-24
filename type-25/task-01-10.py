from functools import reduce 
k = 0

for n in range(200000001, 1000000000):
    my_l = []
    for x in range(2, int(n ** 0.5) + 1):
        if n % x == 0:
            my_l.append(x)
            my_l.append(n // x)
            if len(my_l) >= 10:
                break

    if (len(my_l) > 5):
        my_l.sort()
        m = reduce(lambda a, b: a * b, my_l[:5], 1)
        if 0 < m < n:
            k += 1
            print(m)
            if k == 5:
                break