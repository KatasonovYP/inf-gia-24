def f(x, y):
    if x > y:
        return 0
    if x == y:
        return 1
    else:
        return f(x + 2, y) + f(x * 2, y)

print(f(1, 18) * f(18, 52))