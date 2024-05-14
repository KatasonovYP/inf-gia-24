f = open("type-27/2022-real-02/A.txt")
n, road_len, packet_volume, robot_charge = list(map(int, f.readline().split()))
a = [0] * road_len

# считаем считываем данные с файла
for i in range(n):
    kilometer_num, daily = list(map(int, f.readline().split()))
    a[kilometer_num % road_len] = daily // packet_volume + (daily % packet_volume > 0)

max_s = sum(a)
# если у робота хватает заряда
if robot_charge < (road_len + 1) // 2 - 1:
    c = sum(a[: robot_charge * 2 + 1])
    # если на этом километре есть дом, то размещаем в нем почтовое отделение
    if a[robot_charge]:
        max_s = c
    else:
        max_s = 0
    print(f'{max_s=}')

    # повторяем действия для всех километров кольцевой дороги
    for i in range(1, road_len):
        # пересчитываем сумму после перемещения почтового отделения на 1 км вперед
        c += a[(i + robot_charge * 2) % road_len] - a[i - 1]
        # если на следующем километре есть дом, то проверяем и переписываем максимум
        if a[(i + robot_charge) % road_len]:
            max_s = max(max_s, c)
            print(f'{max_s=}')

print(max_s)
