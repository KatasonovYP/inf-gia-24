def mod(n, m):
    return n % m == 0

def f(x, A):
    return not mod(x, A) <= (mod(x, 6) <= (not mod(x, 4)))

limit = 1000

# # cпособ 1 (счетчик)
# for A in range(1, limit):
#     count = 0
#     for x in range(0, limit):
#         if f(x, A):
#             count += 1
#     if count == limit:
#         print(A)


# # cпособ 2 (флаг)
# for A in range(1, limit):
#     flag = True
#     for x in range(1, limit):
#         if f(x, A):
#             flag = False
#             break
#     if flag:
#         print(A)


# способ 3 (all)
for A in range(1, limit):
    if all(f(x, A) for x in range(1, limit)):
        print(A)