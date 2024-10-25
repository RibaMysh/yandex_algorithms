def max_satisfied_children(n, greed_factors, m, cookie_sizes):

    greed_factors.sort()
    cookie_sizes.sort()

    child_index = 0
    cookie_index = 0
    satisfied_children = 0


    while child_index < n and cookie_index < m:

        if cookie_sizes[cookie_index] >= greed_factors[child_index]:
            satisfied_children += 1
            child_index += 1

        cookie_index += 1

    return satisfied_children


n = int(input())
greed_factors = list(map(int, input().split()))
m = int(input())
cookie_sizes = list(map(int, input().split()))

print(max_satisfied_children(n, greed_factors, m, cookie_sizes))