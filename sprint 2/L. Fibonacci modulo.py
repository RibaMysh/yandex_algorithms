def f(n, k):
    if n == 0 or n == 1:
        return 1 % (10 ** k)
    fib = [0] * (n + 1)
    fib[0], fib[1] = 1, 1

    mod = 10 ** k

    for i in range(2, n + 1):
        fib[i] = (fib[i - 1] + fib[i - 2]) % mod

    return fib[n]


n, k = map(int, input().split())
print(
    f(n, k)
)
