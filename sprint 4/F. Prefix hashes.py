def fast_pow(a, n, m):
    result = 1
    while n > 0:
        if n % 2 == 1:
            result = (result * a) % m
        a = (a * a) % m
        n //= 2
    return result

a = int(input())
m = int(input())
s = input()
t = int(input())

n = len(s)

# Массив для хранения префиксных хешей
hashes = [0] * (n + 1)

# Массив для хранения степеней числа a
powers = [1] * (n + 1)

# Предвычисление хешей и степеней
for i in range(1, n + 1):
    hashes[i] = (hashes[i - 1] * a + ord(s[i - 1])) % m
    powers[i] = (powers[i - 1] * a) % m

# Обработка запросов
for _ in range(t):
    l, r = map(int, input().split())
    l -= 1  # Приведение к 0-индексации
    hash_value = (hashes[r] - hashes[l] * powers[r - l] % m + m) % m
    print(hash_value)
