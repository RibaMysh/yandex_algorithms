n = int(input())
m = int(input())
matrix = [input().split() for _ in range(n)]

for i in range(m):
    for j in range(n):
        print(matrix[j][i], end=" ")
    print()

