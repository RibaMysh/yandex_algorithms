#https://contest.yandex.ru/contest/22450/run-report/115380245/

def best_place(houses: list, n: int) -> None:
    left_ans = list()
    right_ans = list()
    right_counter = left_counter = n

    for i in range(n):
        right_index = n - i - 1

        if houses[i] == 0:
            left_counter = 0
        else:
            left_counter += 1
        left_ans.append(left_counter)

        if houses[right_index] == 0:
            right_counter = 0
        else:
            right_counter += 1
        right_ans.append(right_counter)

    for i in range(n):
        print(min(right_ans[n - i - 1], left_ans[i]), end=' ')


n = int(input())
houses = list(map(int, input().split()))
best_place(houses, n)
