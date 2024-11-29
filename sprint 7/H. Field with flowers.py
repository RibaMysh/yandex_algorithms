def solution(flowers, n, m):
    dp = [[0] * m for _ in range(n)]
    dp[n - 1][0] = flowers[n - 1][0]

    for i in range(n - 2, -1, -1):
        dp[i][0] = dp[i + 1][0] + flowers[i][0]

    for i in range(1, m):
        dp[n - 1][i] = dp[n - 1][i - 1] + flowers[n - 1][i]

    for i in range(n - 2, -1, -1):
        for j in range(1, m):
            dp[i][j] = flowers[i][j] + max(dp[i + 1][j], dp[i][j - 1])

    return dp[0][m - 1]


n, m = map(int, input().split())
flowers = [[int(i) for i in input()] for _ in range(n)]
print(solution(flowers, n, m))
