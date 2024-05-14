
f = open('24.txt', 'r')
s = f.readline()
s = "ABC" + s + "ABC" #добавляем разделители в начале и конце
max_l = 0
delim = [] #создаём список из позиций разделителей
for i in range(len(s) - 2):
    if set(s[i:i+3]) == set(['A', 'B', 'C']): #проверяем тройку на разделитель
        delim.append(i) #добавляем в список позицию разделителя
for j in range(len(delim) - 1):
    max_l = max(max_l, delim[j + 1] - delim[j] - 3) #находим максимальный фрагмент
print(max_l)