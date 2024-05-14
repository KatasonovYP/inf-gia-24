mind = 10**10

for a1 in range(20, 120):
    for a2 in range(a1 + 1, 120):
        for x in range(20, 120):
            if (
                (47 <= x <= 115)
                <= (not (a1 <= x <= a2) and (24 <= x <= 90))
                <= (not (47 <= x <= 115))
            ) == 0:
                break
            else:
                mind = min(mind, a2 - a1)

print(mind)
