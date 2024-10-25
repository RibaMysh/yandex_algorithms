def bs(arr):
    is_sort = True
    for i in range(len(arr) - 1):
        swapped = False
        for j in range(1, len(arr) - i):
            if arr[j - 1] > arr[j]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
                swapped = True
                is_sort = False
        if swapped:
            print(*arr)
        else:
            break
    if is_sort:
        print(*arr)


n = int(input())
arr = list(map(int, input().split()))
bs(arr)
