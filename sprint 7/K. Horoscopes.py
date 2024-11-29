def solution(n, A, m, B):
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if A[i - 1] == B[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    print(dp[n][m])
    if dp[n][m] == 0:
        return

    i_indices = []
    j_indices = []
    i, j = n, m
    while dp[i][j] != 0:
        if A[i - 1] == B[j - 1]:
            i_indices.append(i)
            j_indices.append(j)

            i -= 1
            j -= 1
        else:
            if dp[i][j] == dp[i - 1][j]:
                i -= 1
            else:
                j -= 1

    print(*i_indices[::-1], end=' ')
    print()
    print(*j_indices[::-1], end=' ')


n = int(input())
A = input().split()
m = int(input())
B = input().split()
solution(n, A, m, B)
