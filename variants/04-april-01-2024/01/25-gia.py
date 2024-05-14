for i in range(101_000_000, 102_000_000 + 1, 2):
    count = 1
    for j in range(2, round(i ** 0.5) + 1):
        if i % j == 0:
            if j % 2 == 0:
                count += 1
            k = i // j
            if k % 2 == 0:
                count += 1
                if j == k:
                    count -= 1
            if count > 3:
                break
    if count == 3:
        print(i)