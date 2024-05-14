from itertools import permutations

def algo(s: str):
    while not '00' in s:
        if '011' in s:
            s = s.replace('011', '101', 1)
        else:
            s = s.replace('01', '40', 1)
            s = s.replace('02', '20', 1)
            s = s.replace('022', '1401', 1)
    return s


n = 2
s = '1' * n + '2' * n
for p in list(permutations(s)):
    print(''.join(p))

# for i in range(2, 2**30):
#     s = bin(i)[2:]
#     if s.count('0') == s.count('1'):
#         s = '0' + s.replace('0', '2') + '0'
#         res = algo(s)
#         if res.count('1') == 8 and res.count('2') == 13:
#             print(res.count('4'), res)
