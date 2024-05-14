with open("24.txt") as f:
    data = f.readline()

digits = "6789"
letters = "ABC"

mx = 0
current = 1

for i in range(len(data) - 1):
    if (
        data[i] in letters
        and data[i + 1] in letters
        or data[i] in digits
        and data[i + 1] in digits
    ):
        mx = max(mx, current)
        current = 1
    else:
        current += 1

print(mx)
