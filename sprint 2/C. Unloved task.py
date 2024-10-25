import os

LOCAL = os.environ.get('REMOTE_JUDGE', 'false') != 'true'

if LOCAL:
    class Node:
        def __init__(self, value, next_item=None):
            self.value = value
            self.next_item = next_item


def node_by_index(head, index):
    if index == 0:
        return head
    for i in range(index):
        head = head.next_item
    return head


def solution(node, idx):
    if idx == 0:
        return node.next_item
    previous_node = node_by_index(node, idx - 1)
    previous_node.next_item = node_by_index(node, idx + 1)
    return node


def test():
    node3 = Node("node3", None)
    node2 = Node("node2", node3)
    node1 = Node("node1", node2)
    node0 = Node("node0", node1)
    # node0 -> node1 -> node2 -> node3
    new_head = solution(node0, 1)
    assert new_head is node0
    assert new_head.next_item is node2
    assert new_head.next_item.next_item is node3
    assert new_head.next_item.next_item.next_item is None
    # result is node0 -> node2 -> node3


if __name__ == '__main__':
    test()
