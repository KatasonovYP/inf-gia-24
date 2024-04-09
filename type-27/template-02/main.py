n = [
    sorted(list(map(int, a.split(" ")))) for a in open("27-.txt").readlines()[1:]
]  # массив отсортированных чисел в тройках

sum_min = sum([a[0] for a in n])
sum_aver = sum([a[1] for a in n])
sum_max = sum([a[2] for a in n])

if sum_min % 2 == sum_aver % 2:
    d = max(
        [a[1] - a[2] for a in n if a[1] % 2 != a[2] % 2]
        + [a[0] - a[2] for a in n if a[0] % 2 != a[2] % 2]
    )  # максимальная выгода, которую можно получить после перестановки чисел
    print(d)
    sum_max += d

print(sum_max)
