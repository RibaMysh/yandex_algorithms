import os

LOCAL = os.environ.get('REMOTE_JUDGE', 'false') != 'true'

if LOCAL:
    class Node:
        def __init__(self, value, left=None, right=None):
            self.value = value
            self.right = right
            self.left = left


def solution(root) -> int:
    mx = - 10 ** 9
    mx = max(mx, root.value)
    if root.left is not None:
        mx = max(mx, solution(root.left))

    if root.right is not None:
        mx = max(mx, solution(root.right))

    return mx


def test():
    node1 = Node(1)
    node2 = Node(-5)
    node3 = Node(3, node1, node2)
    node4 = Node(2, node3, None)
    assert solution(node4) == 3


if __name__ == '__main__':
    test()
