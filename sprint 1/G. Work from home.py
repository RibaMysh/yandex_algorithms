def bn(n: int) -> int:
    if n == 0:
        return 0
    s = ''
    while n > 0:
        s += str(n % 2)
        n //= 2

    return int(s[::-1])

print(bn(int(input())))
