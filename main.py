# from ipaddress import *
# result = 0

# for ip in ip_network('170.224.7.224/255.255.255.224'):
#     ls = list(map(lambda x: bin(int(x))[2:].zfill(8), str(ip).split('.')))
#     address = '.'.join(ls)
#     if address.count('1') % 4 == 0:
#         result += 1

# print(result)

def trans(n, base):
    result = ''
    while n:
        result += str(n % base)
        n //= base
    return result[::-1]

print(bin(10)[2:])
x = int('255', 7) - int('2110', 3)
y_2 = (x + int('5', 6) * int('71', 9)) / 8
print(y_2 ** (0.5))