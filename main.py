a = sorted(list(map(int, input().split())))
min_farq = abs(a[1] - a[0])
juft = (a[0], a[1])

for i in range(len(a) - 1):
    if abs(a[i+1] - a[i]) < min_farq:
        min_farq = abs(a[i+1] - a[i])
        juft = (a[i], a[i+1])

print(juft)
