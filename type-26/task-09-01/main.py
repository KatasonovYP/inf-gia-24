file = open('data.txt').read()
data = file.split('\n')[1:-1]
data = [line.split() for line in data]
data = [[int(line[0]), int(line[1]) + int(line[0]), line[2]] for line in data]
auto_places = 80
autobus_places = 20

# print(sorted(data)[-10:])

len_time = 1800
time_arrive = [0] * len_time
time_leave_auto = [0] * len_time
time_leave_autobus = [0] * len_time

for [start, finish, auto_type] in data:
    time_arrive[start] = auto_type
    if auto_type == 'A':
        time_leave_auto[finish] -= 1
    else:
        time_leave_autobus[finish] -= 1

stay_auto = 0
stay_autobus = 0
leave = 0
count = 0


for i in range(len_time):
    auto_type = time_arrive[i]
    if auto_type == 'A' and stay_auto + 1 <= auto_places:
        stay_auto += 1
        count += 1
    elif auto_type == 'B' and stay_autobus + 1 <= autobus_places:
        stay_autobus += 1
        count += 1
    else:
        leave += 1
        for jt in data:
            if jt[0] == i:
                if auto_type == 'A':
                    time_leave_auto[jt[1]] += 1
                elif auto_type == 'B':
                    time_leave_autobus[jt[1]] += 1
                break

    print(count, leave)