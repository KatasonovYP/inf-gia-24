with open('./24_demo.txt') as file:
    data = file.read()

count = 1
max_count = 0
for i in range(len(data) - 1):
    if data[i] != data[i + 1]:
        count += 1
    else:
        max_count = max(count, max_count)
        count = 1

max_count = max(count, max_count)

print(max_count)