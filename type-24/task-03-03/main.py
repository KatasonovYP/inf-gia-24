count = 2
maxi = 0

with open("data.txt") as file:
    data = file.readline()

for i in range(2, len(data)):
    if int(data[i - 2]) + int(data[i - 1]) > int(data[i]):
        count += 1
    else:
        maxi = max(maxi, count)
        count = 2

print(maxi)
