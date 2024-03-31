f = list(map(lambda x: x.split(), open("data.txt").readlines()[1:]))


notes = dict(sorted({int(i[0]): [int(i[1]), i[2]] for i in f}.items()))
parking = [[], []]
count, leave = 0, 0

for arrive in notes:
    parking = [list(filter(lambda x: x > arrive, x)) for x in parking]
    if len(parking[0]) != 80 and notes[arrive][1] == "A":
        parking[0].append(arrive + notes[arrive][0])
        count += 1
    elif len(parking[1]) != 20:
        parking[1].append(arrive + notes[arrive][0])
        count += 1 if notes[arrive][1] == "A" else 0
    else:
        leave += 1

print(count, leave)
