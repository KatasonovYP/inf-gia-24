a = {
    'apple': 'green',
    'pineapple': 'yellow',
    'orange': 'orange',
}

repeats = dict()

s = '123423415143531'

for char in s:
    if char in repeats:
        repeats[char] += 1
    else:
        repeats[char] = 1

print(repeats)