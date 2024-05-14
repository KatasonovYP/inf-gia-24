for it in range(101_000_000, 102_000_000 + 1, 2):
    cou = 1
    for y in range(2, round(it ** 0.5) + 1):
        if it % y == 0 and y % 2 == 0:
            cou += 1
        k = it // y
        if it % k == 0 and k % 2 == 0:
            cou += 1
            if k == y:
                cou -= 1
        if cou > 3:
            break

    if cou == 3:
        print(it)