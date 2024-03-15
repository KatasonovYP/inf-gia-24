### решу ЕГЭ
# f = [int(x) for x in open("17.txt")]
# MINI = min([x for x in f if str(x)[-2] == str(x)[-1]])
# count, maxi = 0, -999999
# for i in range(0, len(f) - 1):
#     x, y = f[i], f[i + 1]
#     if (str(x)[-1] == str(y)[-2]) or (str(x)[-2] == str(y)[-1]):
#         if (f[i] % 7) != (f(i + 1) % 7):
#             if (x**2 + y**2) <= MINI**2:
#                 count += 1
#                 maxi = max(maxi, x**2 + y**2)
# print(count, maxi)

###

file = open("17.txt")
data = [int(i) for i in file]

print(data)

maxi = data[0]
mini = data[0]
max_sum = data[0]
count = 0

for it in data:
    it_len = len(str(it))
    if it < 0:
        it_len -= 1
    if it_len >= 2:
        if str(it)[-2] == str(it)[-1]:
            mini = min(mini, it)

# print(mini)

for i in range(len(data) - 1):
    last_1 = str(data[i])[-1]
    prelast_1 = str(data[i])[-2]
    last_2 = str(data[i + 1])[-1]
    prelast_2 = str(data[i + 1])[-2]

    if (last_1 == prelast_2) or (last_2 == prelast_1):
        if (data[i] % 7 == 0) != (data[i + 1] % 7 == 0):
            sm = data[i] ** 2 + data[i + 1] ** 2
            if sm <= mini ** 2:
                count += 1
                max_sum = max(max_sum, sm)

print(count, max_sum)
