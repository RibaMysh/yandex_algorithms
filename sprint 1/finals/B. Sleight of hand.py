#https://contest.yandex.ru/contest/22450/run-report/115478318/

k = int(input())
matrix = []
counter = dict()
for i in range(4):
    for num in input():
        if num != '.':
            counter[num] = counter.get(num, 0) + 1
final_counter = 0
for i in range(1, 10):
    i = str(i)
    if i in counter:
        if counter[str(i)] <= 2 * k:
            final_counter += 1
print(final_counter)
