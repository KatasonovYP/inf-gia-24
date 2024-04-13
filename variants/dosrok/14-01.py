import string
for x in '0123456789abcdefghijklmnopq':
    ch1 = int(f'123{x}24', 27)
    ch2 = int(f'135{x}78', 27)
    s = ch1 + ch2
    if s % 26 == 0:
        print(x, s // 26)
# 1213206
# 3972499
# for x in range(27):
#     ch1 = int('123024', 27) + x * 27**2
#     ch2 = int('135078', 27) + x * 27**2
#     s = ch1 + ch2
#     if s % 26 == 0:
#         print(x, s // 26)

