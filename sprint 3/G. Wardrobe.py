n = int(input())
lst = input().split()
ans = [0] * 3
for color in lst:
    ans[int(color)] += 1

for i in range(3):
    for j in range(ans[i]):
        print(i, end=' ')
