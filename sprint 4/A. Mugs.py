d = dict()
k = 0
for i in range(int(input())):
    name = input()
    if name not in d:
        d[name] = k
        k += 1

for i in sorted(d.items(), key=lambda x: x[1]):
    print(i[0])

