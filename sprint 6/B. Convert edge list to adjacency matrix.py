v, e = map(int, input().split())
matrix = [[0] * v for _ in range(v + 1)]

for _ in range(e):
    v1, v2 = map(int, input().split())
    matrix[v1][v2 - 1] = 1

for i in range(1, v + 1):
    print(*matrix[i])
