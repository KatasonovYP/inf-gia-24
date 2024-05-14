for it in range(101_000_000, 102_000_000 + 1, 2):
    seps = [it]
    
    for d in range(2, round(it ** 0.5) + 1):
        if it % d == 0:
            if d % 2 == 0:
                seps.append(d)
            k = it // d
            if k % 2 == 0:
                seps.append(k)
                if k == d:
                    seps.pop()
        if len(seps) > 3:
            break

    if len(seps) == 3:
        print(it, seps)