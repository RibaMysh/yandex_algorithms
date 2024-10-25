import os

LOCAL = os.environ.get('REMOTE_JUDGE', 'false') != 'true'

if LOCAL:
    class Node:
        def __init__(self, value, left=None, right=None):
            self.value = value
            self.right = right
            self.left = left


def height(root, counter) -> int:
    counter += 1
    if root is None:
        return counter

    return max(height(root.left, counter), height(root.right, counter))


def solution(root) -> bool:
    if root is None:
        return True

    if abs(height(root.left, 0) - height(root.right, 0)) > 1:
        return False

    return solution(root.left) and solution(root.right)


def test():
    node1 = Node(1)
    node2 = Node(-5)
    node3 = Node(3, node1, node2)
    node4 = Node(10)
    node5 = Node(2, node3, node4)
    assert solution(node5)


if __name__ == '__main__':
    test()
