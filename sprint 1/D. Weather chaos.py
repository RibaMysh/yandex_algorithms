def weather_randomness(n, lst):
    if n == 1:
        return 1
    k = 0
    if lst[0] > lst[1]:
        k += 1
    if lst[-1] > lst[-2]:
        k += 1
    for i in range(1, n - 1):
        if lst[i] > lst[i - 1] and lst[i] > lst[i + 1]:
            k += 1
    return k


n = int(input())
lst = list(map(int, input().split()))
print(weather_randomness(n, lst))
