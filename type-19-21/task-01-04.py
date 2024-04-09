from functools import lru_cache

def moves(a):
    return a + 1, a ** 2


@lru_cache(None)
def game(a):
    if a >= 100: return "W"
    if any(game(x) == "W" for x in moves(a)): return "P1"
    if any(game(x) == "P1" for x in moves(a)): return "V1"

for s in range(2, 99):
    if game(s) == "V1":
        print(s, game(s))