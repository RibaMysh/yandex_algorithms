n, m = map(int, input().split())
ans = dict()
for i in range(m):
    v1, v2 = input().split()
    lst = ans.get(v1, [])
    lst.append(v2)
    ans[v1] = lst

for i in range(n):
    lst = ans.get(str(i + 1), [])
    if len(lst) == 0:
        print(0)
    else:
        print(len(lst), *lst)
