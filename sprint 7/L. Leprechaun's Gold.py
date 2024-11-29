def solution(m, gold):
    dp = [0] * (m + 1)

    for item in gold:
        for j in range(m, item - 1, -1):
            if dp[j - item] + item > dp[j]:
                dp[j] = dp[j - item] + item

    print(dp[m])


n, m = map(int, input().split())
gold = list(map(int, input().split()))
solution(m, gold)
