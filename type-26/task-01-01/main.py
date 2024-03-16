s = [i for i in open('26.txt').readlines()]
size = int(s[0].split()[0])
files = [int(i) for i in s[1:]]
files = sorted(files)
summa = 0
counter = 0
itog = 0

for file in files:
    if summa + file > size:
        break
    summa += file
    counter += 1

zapas = size - summa

# [1, 1, 1, 4, 7, 7, 8]
print(files[:counter])
print(zapas)


for i in range(len(files)):
    if files[i] - files[counter] <= zapas:
        itog = files[i]

print(counter, itog)