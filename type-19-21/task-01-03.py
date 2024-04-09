from functools import lru_cache

def moves(a):
    return list(filter(lambda x: x % 3, [a + 1, a + 2, a * 2]))

@lru_cache(None)
def game(a):
    if a >= 103: return "W"
    if any(game(x) == "W" for x in moves(a)): return "P1"
    if all(game(x) == "P1" for x in moves(a)): return "V1"
    if any(game(x) == "V1" for x in moves(a)): return "P2"
    if all(game(x) in ("P1", "P2") for x in moves(a)): return "V12"

for s in range(1, 200):
    if  s % 3 and game(s) == "V12":
        print(s, game(s))