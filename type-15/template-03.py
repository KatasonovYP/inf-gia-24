limit = 300

def f(x, y, a):
    return ((x <= 9) <= (x * x <= a)) and ((y*y <= a) <= (y <= 9))

# for a in range(limit, 1, -1): 
#     k = 0
#     for x in range(0, limit):
#         for y in range(0, limit):
#             if not f(x, y, a):
#                 break
#         if not f(x, y, a):
#             break
        
#     else:
#         print(a)
#         break

for a in range(0, limit):
    if all(f(x, y, a) for x in range(0, limit) for y in range(0, limit)):
        print(a)
