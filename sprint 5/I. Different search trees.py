from math import factorial as f

n = int(input())

print(
    f(2 * n) // (f(n + 1) * f(n))

)
