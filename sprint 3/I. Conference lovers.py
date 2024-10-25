n = int(input())
lst = list(map(int, input().split()))
k = int(input())

counter = dict()
for num in lst:
    counter[num] = counter.get(num, 0) + 1

ki = 0
for key, v in sorted(counter.items(), key=lambda x: (-x[1], x[0])):
    if ki == k:
        break
    print(key, end=' ')
    ki += 1
