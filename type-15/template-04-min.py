# P = [5, 30] и Q = [14, 23]

P = list(range(20, 50 + 1))
Q = list(range(30, 65 + 1))

a = 0
b = 100

A = []

for x in range(a, b + 1):
    f = (not (x in A)) <= ((x in P) <= (not (x in Q)))
    if not f:
        A.append(x)

print(A)