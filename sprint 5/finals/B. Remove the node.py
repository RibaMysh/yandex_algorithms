"""

ПРИНЦИП РАБОТЫ

Принцип работы удаления узла в BST делится на два шага:
- найти подходящий узел для замены удаляемого;
- поставить найденный узел на место удаляемого (а также позаботиться о его левом потомке, если он есть).

Для простоты рассуждений будем считать, что мы уже нашли узел для удаления и находимся в случае,
когда у удаляемого узла есть 2 потомка.
Все остальные случаи я обработал отдельно и пометил комментариями.

Рассмотрим каждый шаг по отдельности.
Для нахождения подходящего узла я выбираю наибольший элемент в левом поддереве.
Затем меняю значения найденного и удаляемого узлов, переназначая левого потомка (если он есть) родителю найденного узла.

ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ

1. На вход программа получает сначала n — число различных узлов, далее идут n строк вида:
    <id узла> <значение> <id левого потомка> <id правого потомка>.
После n строк вводится значение удаляемого узла.

2. Алгоритм поочередно обрабатывает все возможные случаи и завершает выполнение, когда один из них решён.

3. Алгоритм завершает работу после обработки одного из случаев и возвращает корень нового дерева.

ВРЕМЕННАЯ СЛОЖНОСТЬ

Пусть h — высота дерева.

Затраченная память:
Дополнительной памяти не было выделено, кроме хранения двух родителей и двух узлов.
Таким образом, можно сказать, что затраты памяти составляют O(1).

Затраченное время:
Алгоритм использует функцию remove, которая, в свою очередь, использует две другие функции: find_left_max и find_node.
Рассмотрим эти функции:
    - find_node — функция ищет узел по заданному ключу и возвращает его вместе с родителем найденного узла.
    В худшем случае функция работает за O(h), если нужный узел находится на листе.
    Однако рассмотрим абстрактный случай и предположим, что функция нашла узел на i-й "глубине" дерева.

    - find_left_max — функция принимает левое поддерево узла и возвращает максимальный элемент этого поддерева
    вместе с родителем.
    В худшем случае функция работает за O(h-1), если запуск выполняется от корня дерева.
    Однако мы рассмотрим абстрактный случай и предположим, что максимум найден на j-й глубине.

    Так как в алгоритме функция find_left_max всегда вызывается для элемента, который нашла функция find_node,
    их суммарное время работы составляет O(i + j).
    В худшем случае find_left_max дойдёт до нижнего уровня, и тогда сумма O(i + j) в худшем случае равна O(h).

Так как мы установили, что худшее время работы функций find_left_max и find_node составляет O(h),
худшее время работы функции remove также равно O(h).

"""

# id: 119969800

from typing import Optional
import os

LOCAL = os.environ.get('REMOTE_JUDGE', 'false') != 'true'

if LOCAL:
    class Node:
        def __init__(self, left=None, right=None, value=0):
            self.right = right
            self.left = left
            self.value = value
else:
    from node import Node


def find_left_max(node, parent):
    while node.right is not None:
        parent = node
        node = node.right
    return node, parent


def find_node(node, parent, key):
    while node is not None:
        if key > node.value:
            parent = node
            node = node.right
        elif key < node.value:
            parent = node
            node = node.left
        else:
            return node, parent
    return None, None


def remove(root, key) -> Optional[Node]:
    main_node, parent = find_node(root, None, key)

    if main_node is None:
        return root

    # удаляемый узел - лист
    # child free узел:)
    if main_node.left is None and main_node.right is None:
        # удаляемый узел - корень
        if parent is None:
            return None
        if parent.left == main_node:
            parent.left = None
            return root
        parent.right = None
        return root

    # у удаляемого узла - один потомок
    if main_node.left is None or main_node.right is None:
        child = main_node.left if main_node.left is not None else main_node.right

        # удаляемый узел - корень с одним ребенком
        if parent is None:
            return child

        if parent.left == main_node:
            parent.left = child
            return root
        parent.right = child
        return root

    # удаляем узел с двумя детьми
    second_node, second_parent = find_left_max(main_node.left, main_node)

    # заменяем значение удаляемого узла на значение подходящего
    main_node.value = second_node.value

    # удаляем узел второй узел и переносим его ребенка(если он есть)

    if second_parent.left is second_node:
        second_parent.left = second_node.left
    else:
        second_parent.right = second_node.left
    return root


def test():
    node1 = Node(None, None, 2)
    node2 = Node(node1, None, 3)
    node3 = Node(None, node2, 1)
    node4 = Node(None, None, 6)
    node5 = Node(node4, None, 8)
    node6 = Node(node5, None, 10)
    node7 = Node(node3, node6, 5)
    new_head = remove(node7, 10)
    assert new_head.value == 5
    assert new_head.right is node5
    assert new_head.right.value == 8


if __name__ == '__main__':
    test()
