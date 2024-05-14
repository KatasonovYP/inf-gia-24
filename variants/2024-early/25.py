import re


count = 0
for i in range(0, 10**10, 2024):
    if re.fullmatch('1\d*2322\d?2', f'{i}'):
        print(i, i // 2024)
        count += 1

print(f'{count=}')
