n = int(input())
lst = sorted(map(int, input().split()), reverse=True)
for i in range(n - 2):
    current_mx = lst[i]
    if current_mx < lst[i + 1] + lst[i + 2]:
        print(current_mx + lst[i + 1] + lst[i + 2])
        break
