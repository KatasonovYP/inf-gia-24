a = [1, 2, -1, -20]


for i in range(len(a)):
    for j in range(i + 1, len(a)):
        if a[i] > a[j]:
            [a[i], a[j]] = [a[j], a[i]]

# 1 цикл - сложность O(n)
# вложенный цикл - сложность O(n^2)
# вложенный цикл - сложность O(n * log(n))
            

print(a)