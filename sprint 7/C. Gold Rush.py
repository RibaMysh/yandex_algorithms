def find_mx(weights, m: int) -> int:
    ans = 0
    for value, weight in weights:
        if weight <= m:
            ans += weight * value
            m -= weight
        else:
            ans += m * value
            return ans
    return ans


m = int(input())
n = int(input())
weights = sorted([list(map(int, input().split())) for _ in range(n)],
                 key=lambda x: x[0], reverse=True)
print(find_mx(weights, m))
