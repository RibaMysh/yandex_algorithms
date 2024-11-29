def solution(flowers, n, m):
    dp = [[float(0) for _ in range(m + 1)] for _ in range(n)]
    for i in range(n):
        dp[i][0] = float('-inf')

    dp.append([float('-inf')] * (m + 1))

    dp[n - 1][1] = flowers[n - 1][0]
    for i in range(n - 1, -1, -1):
        for j in range(1, m + 1):
            if i == n - 1 and j == 1:
                continue
            dp[i][j] = flowers[i][j - 1] + max(dp[i + 1][j], dp[i][j - 1])

    print(dp[0][m])
    
    road = []
    l, c = 0, m
    while l != n - 1 or c != 1:
        if dp[l + 1][c] > dp[l][c - 1]:
            l += 1
            road.append('U')
        else:
            c -= 1
            road.append('R')
    print(*road[::-1], sep='')


n, m = map(int, input().split())
flowers = [[int(i) for i in input()] for _ in range(n)]
solution(flowers, n, m)
