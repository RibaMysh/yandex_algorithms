def binary_search(arr: list, target: int, left, right, found):
    if right <= left:
        return found

    mid = (left + right) // 2

    if arr[mid] >= target:
        return binary_search(arr, target, left, mid, mid + 1)
    return binary_search(arr, target, mid + 1, right, found)


n = int(input())
arr = list(map(int, input().split()))
target = int(input())
print(binary_search(arr, target, 0, n, -1),
      binary_search(arr, target * 2, 0, n, -1))
