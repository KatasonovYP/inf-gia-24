for x in range(0, 257):
    if 114 & x == 96:
        print(x, bin(x)[2:].zfill(8))
