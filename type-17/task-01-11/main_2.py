f = [abs(int(i)) for i in open("17.txt")]
max_element = max(f, key=lambda x: x if x % 10 == 3 else -10_000) ** 2
print(max_element)