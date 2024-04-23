from functools import reduce

with open('26.txt') as file:
    data = file.read().split('\n')
    money = int(data[0].split(' ')[1])
    data = data[1:-1]
    for i in range(len(data)):
        [cost, lineType] = data[i].split(' ')
        data[i] = {
            'type': lineType,
            'cost': int(cost),
        }

data = sorted(data, key=lambda x: x['cost'], reverse=True)

sum_func = lambda a, b: a + b['cost']

selected = []

for i in range(len(data)):
    item = data.pop()
    if reduce(sum_func, selected, 0) + item['cost'] <= money:
        selected.append(item)
    else:
        data.append(item)
        break

selected = sorted(selected, key=lambda x: x['type'])
data = sorted(data, key=lambda x: x['type'], reverse=True)

for i in range(len(selected)):
    item = data[-1]
    if reduce(sum_func, selected[:-1], 0) + item['cost'] <= money:
        selected.pop()
        selected.insert(0, data.pop())
    else:
        break

print(len(list(filter(lambda x: x['type'] == 'A', selected))), money - reduce(sum_func, selected, 0))
