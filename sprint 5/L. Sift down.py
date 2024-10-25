def sift_down(heap, idx) -> int:
    heap_max_index = len(heap) - 1
    left_child = 2 * idx
    right_child = 2 * idx + 1

    if left_child > heap_max_index:
        return idx

    if right_child <= heap_max_index and heap[left_child] < heap[right_child]:
        mx_idx = right_child
    else:
        mx_idx = left_child

    if heap[idx] < heap[mx_idx]:
        heap[idx], heap[mx_idx] = heap[mx_idx], heap[idx]
        return sift_down(heap, mx_idx)
    return idx


def test():
    sample = [-1, 12, 1, 8, 3, 4, 7]
    assert sift_down(sample, 2) == 5


if __name__ == '__main__':
    test()
