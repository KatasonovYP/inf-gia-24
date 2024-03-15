from functools import reduce


def split_to_ints(x):
    return list(map(int, x.split(" ")))


result = [0] * 7 * 24 * 60 * 60

with open("./data.txt") as file:
    data = file.read().split("\n")
    data = list(map(split_to_ints, data[1:-1]))


week_start = 1634515200
week_finish = week_start + len(result)
count = 0

for [process_start, process_finish] in data:
    if process_start < week_start and (week_start < process_finish or process_finish == 0):
        count += 1
    if week_start <= process_start <= week_finish:
        result[process_start - week_start] += 1
    if week_start <= process_finish <= week_finish:
        result[week_start - process_finish] -= 1

max_count = count
current_time = 0
max_time = 0

print(count)

for it in result:
    max_count = max(count, max_count)
    count += it

for it in result:
    if count == max_count:
        max_time += 1
    count += it
    

print(max_time, max_count)

# [0 0 0 1 3 0 -1 1 0 2 -3]
#  3 3 3 4 7 7 6  7 7 9 6

# 0 0 0 4 4 4 0 0 4