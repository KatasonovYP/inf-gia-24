k = 0

for n in range(460_000_000 + 1, 700_000_000):
    my_l = []
    for x in range(2, int(n ** 0.5) + 1):
        if n % x == 0:
            my_l.append(x)
            my_l.append(n // x)
            if len(my_l) >= 10:
                break
    
    if len(my_l) >= 5:
        k += 1
        print(sorted(my_l, reverse=True)[4])
        if k == 5:
            break

