data = [3, 8, 14, 11, 2]


cnt = 0
max_mean = data[0]

for i in range(len(data)):
    for j in range(i + 1, len(data)):
        mean = (data[i] + data[j]) / 2
        if mean == round(mean) and mean in data:
            cnt += 1
            print(data[i], data[j])
            max_mean = max(int(mean), max_mean)

print(cnt, max_mean)
