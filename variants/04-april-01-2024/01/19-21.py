from functools import lru_cache


def moves(h):
    [a, b] = h
    return (a - 1, b), (a // 2, b), (a, b - 1), (a, b // 2)

@lru_cache(None)
def game(h):
    if (0 in h): return None
    if sum(h) <= 20: return 'W'
    if any(game(x) == 'W' for x in moves(h)): return 'P1'
    if all(game(x) == 'P1' for x in moves(h)): return 'V1'
    if any(game(x) == 'V1' for x in moves(h)): return 'P2'
    if all(game(x) in ('P1', 'P2') for x in moves(h)): return 'V12'


for s in range(10, 100):
    if (game((10, s)) == 'V12'):
        print(s, game((10, s)))