def solution(n, arr):
    d = {0: -1}
    result = 0
    current_diff = 0
    for i in range(n):
        if arr[i] == 0:
            current_diff += 1
        else:
            current_diff -= 1

        if current_diff in d:
            left = d[current_diff]
            new_res = i - left
            result = max(result, new_res)
        else:
            d[current_diff] = i
    return result

n = int(input())
lst = list(map(int, input().split()))
print(solution(n, lst))
