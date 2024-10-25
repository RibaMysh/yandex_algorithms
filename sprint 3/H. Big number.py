def less(num1, num2):
    if num1 + num2 >= num2 + num1:
        return False
    return True


def insertion_sort_by_comparator(array, compare):
    for i in range(1, len(array)):
        item_to_insert = array[i]
        j = i
        while j > 0 and compare(item_to_insert, array[j - 1]):
            array[j] = array[j - 1]
            j -= 1
        array[j] = item_to_insert
    return array[::-1]


n = int(input())
arr = input().split()
arr = insertion_sort_by_comparator(arr, less)
print(''.join(arr))
