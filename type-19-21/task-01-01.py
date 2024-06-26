from functools import lru_cache


def moves(a):
    return a + 1, a + 4, a * 5

@lru_cache(None)
def game(a):
    if a >= 68: return 'W'
    if any(game(x) == 'W' for x in moves(a)): return 'P1'
    if all(game(x) == 'P1' for x in moves(a)): return 'V1'
    if any(game(x) == 'V1' for x in moves(a)): return 'P2'
    if all(game(x) in ('P1', 'P2') for x in moves(a)): return 'V12'


for i in range(1, 200):
    if (game(i) == 'V12'):
        print(i, game(i))