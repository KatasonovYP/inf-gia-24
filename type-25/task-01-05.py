import math

count = 0
answer = []

for i in range(1_000_000, 2_000_000 + 1):
    if (i % 1000 == 0):
        print(i)
    count = 0
    for x in range(900, int(math.sqrt(i)) + 1):
        if i % x == 0:
            y = i // x
            if (y - x <= 100):
                count += 1
            if (count == 3):
                answer.append(i)
                break

print(answer)