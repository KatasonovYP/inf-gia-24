with open("data.txt") as file:
    s = file.readline()

mx = 0

p = [-1] + [i for i in range(len(s) - 1) if s[i] + s[i + 1] == "WW"] + [len(s) - 1]

for i in range(0, len(p) - 101):
    mx = max(mx, p[i + 101] - p[i])

print(mx)
