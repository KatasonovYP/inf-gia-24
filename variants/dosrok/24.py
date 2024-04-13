with open('24.txt') as f:
    data = f.readline()

digits = '6789'
letters = 'ABC'

'CA8666BB7B7A7A8A9A9778CB8BC'

mx = 0
current = 1

for i in range(len(data) - 1):
    if data[i] in letters and data[i + 1] in letters:
        mx = max(mx, current)
        current = 1
    elif data[i] in digits and data[i + 1] in digits:
        mx = max(mx, current)
        current = 1
    else:
        current += 1

print(mx)