from sys import setrecursionlimit

# from ipaddress import ip_network, ip_address, ip_interface
# result = 0

# for ip in ip_network('170.224.7.224/255.255.255.224'):
#     ls = list(map(lambda x: bin(int(x))[2:].zfill(8), str(ip).split('.')))
#     address = '.'.join(ls)
#     if address.count('1') % 4 == 0:
#         result += 1

# print(result)

# def trans(n, base):
#     result = ''
#     while n:
#         result += str(n % base)
#         n //= base
#     return result[::-1]

# print(bin(10)[2:])
# x = int('255', 7) - int('2110', 3)
# y_2 = (x + int('5', 6) * int('71', 9)) / 8
# print(y_2 ** (0.5))

# alpha = '0123456789ABCD'

# for x in alpha:
#     res = int(f'97968{x}1515', 15) + int(f'7{x}23315', 15)
#     if res % 14 == 0:
#         print(x, res // 14)


# n = 10
# []

a = 5

if a == 5 or a == 7:
    print(True)
else:
    print(False)