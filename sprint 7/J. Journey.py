def solution(seq, n):
    dp = [1] * n
    prev = [i for i in range(n)]
    for i in range(1, n):
        for j in range(i):
            if seq[j] < seq[i] and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
                prev[i] = j

    mx = max(dp)
    print(mx)

    index = dp.index(mx)
    ans = [index + 1]
    for i in range(mx - 1):
        ans.append(prev[index] + 1)
        index = prev[index]
    print(*ans[::-1])


n = int(input())
seq = list(map(int, input().split()))
solution(seq, n)
