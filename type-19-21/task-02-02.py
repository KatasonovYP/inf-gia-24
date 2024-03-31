from functools import lru_cache


def moves(h):
    [a, b] = h
    return (a + 1, b), (a + b, b), (a, b + 1), (a, b + a)


@lru_cache(None)
def game(h):
    if sum(h) >= 67:
        return "W"
    if any(game(x) == "W" for x in moves(h)):
        return "P1"
    if all(game(x) == "P1" for x in moves(h)):
        return "V1"
    if any(game(x) == "V1" for x in moves(h)):
        return "P2"
    if all(game(x) in ("P1", "P2") for x in moves(h)):
        return "V12"


for s in range(1, 200):
    if game((9, s)) == "V12":
        print(s, game((9, s)))
