# P = [5, 30] и Q = [14, 23]

P = list(range(5, 30 + 1))
Q = list(range(14, 23 + 1))

a = 0
b = 100

A = list(range(a, b + 1))

for x in range(a, b + 1):
    f = ((x in P) == (x in Q)) <= (not(x in A))
    if not f:
        A.remove(x)

print(A)

# [5, 14]
# [5, 14)

# 5, 14 -> 14 - 5 = 9
# 23, 30 -> 30 - 23 = 7