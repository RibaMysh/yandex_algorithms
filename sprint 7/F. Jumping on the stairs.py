def dp_stair(n, k):
    if n == 1:
        return 1
    MOD = 10 ** 9 + 7
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        for j in range(1, k + 1):
            if i - j >= 0:
                dp[i] = (dp[i - j] + dp[i]) % MOD
    return dp[n]


n, k = map(int, input().split())
print(dp_stair(n, k))
