n, k = map(int, input().split())
lst = sorted((map(int, input().split())))
ans = 0
for i in lst:
    if k - i >= 0:
        ans += 1
        k -= i
    else:
        break
print(ans)
