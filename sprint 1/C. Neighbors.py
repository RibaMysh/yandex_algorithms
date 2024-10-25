n = int(input())
m = int(input())
matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split())))

ni = int(input())
mi = int(input())

ans = []

if ni > 0:
    ans.append(matrix[ni - 1][mi])
if ni < n - 1:
    ans.append(matrix[ni + 1][mi])
if mi > 0:
    ans.append(matrix[ni][mi - 1])
if mi < m - 1:
    ans.append(matrix[ni][mi + 1])
print(*sorted(ans))
