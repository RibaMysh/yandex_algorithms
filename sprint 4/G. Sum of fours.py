n = int(input())
A = int(input())
numbers = sorted(list(map(int, input().split())))
pairs = dict()
ans = set()
for i in range(n):
    for j in range(i+1, n):
        n1, n2 = numbers[i], numbers[j]
        if n1 + n2 not in pairs:
            pairs[n1 + n2] = []
        pairs[n1 + n2].append((i, j))

for i in range(n):
    for j in range(i+1, n):
        n1, n2 = numbers[i], numbers[j]
        target = A - n1 - n2
        if target in pairs:
            for pair in pairs[target]:
                if pair[0] > j:
                    ans.add ( (numbers[i], numbers[j],
                               numbers[pair[0]], numbers[pair[1]]) )


print(len(ans))
for i in sorted(ans):
    print(*i)
