A = [3, 4, 7, 10, 20, 30]
B = [4, 6, 8, 20, 30]
C = []

result = 1

for x in range(1, 1000):
    F = (x in A) <= (
        (x in A)
        and (x in B)
        or ((not (x in B)) == (x in A) and (x in B))
        and (not (x in A))
    )

    if F == 0:
        print((f'{x=}'))
        result *= x

print(f'{result=}')

