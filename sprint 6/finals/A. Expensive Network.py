"""

ПРИНЦИП РАБОТЫ

Принцип работы алгоритма заключается в нахождении наибольшего расстояния до смежных вершин текущей вершины.
Таким образом нам гарантируется инвариант, что у каждой обработанной вершины уже найдено наибольшее расстояние.
Так же важно понимать, что мы сможем найти наибольший путь не у каждой отдельной вершины, а только у той,
до которой сможем добраться от начальной вершины.

ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ

1. На вход программа получает в первой строке два целых числа - n, m (количество вершин и количество ребер).
    Далее даны m строк вида: "u v w", где u, v - номера вершин, а w - вес дороги между ними.
    Так же перед началом работы алгоритма строиться сам граф в виде списка(таблицы) смежности.
    Затем алгоритм запускается от первой вершины.
2. На каждом этапе работы алгоритм обрабатывает еще не обработанную вершину и
    кладет в приоритетную очередь все его смежные вершины.
3. Алгоритм заканчивает свою работу после того как обработает все вершины, до которых можно добраться из начальной и
    выведет максимальную 'дорогу', если существует остов, в противном случае выведет строку 'Oops! I did it again'

ВРЕМЕННАЯ СЛОЖНОСТЬ

Пусть V - количество вершин, E - количество ребер.

Затраченная память:

Для начала дополнительная память понадобилась для хранения самого графа, что заняло O(V^2)
(в худшем случае у нас будет плотный граф, гед нужно будет для каждой вершины хранить V-1 ребро,
но в среднем случае для разряженного графа потребуется O(V + E) памяти на хранение)

Так же нам понадобятся 2 вспомогательных массива: processed, not_processed; Которые в сумме займут O(V) памяти.

И наконец нам понадобиться приоритетная очередь, которая потребует O(E) памяти в худшем случае.

Подводя итоги можно сказать, что в худшем случае потребуется - O(V^2 + E), но в среднем случае - O(V + E)

Затраченное время:

Для начала нам понадобиться построить сам граф, это займет - O(E * h), где h - скорость вычисления хэша для хэш-таблицы.
Для удобства будем считать, что O(h) = O(1) => сложность построения графа(функции make_graph) = O(E)

Теперь перейдем к самому алгоритму. В худшем случае алгоритму придется пройти по всем вершинам и добавить все ребра в
приоритетную очередь, что займет O(V + log E)

В итоге мы получим сложность алгоритма - O(V + log E)

"""


# id: 122136378

class MaxHeap:
    def __init__(self):
        self.heap = [float('-inf')]
        self.size = 0

    def add(self, el):
        self.heap.append(el)
        self.size += 1
        self.sift_up(self.size)

    def pop_max(self):
        if self.size == 0:
            raise IndexError('Heap is empty')
        res = self.heap[1]
        self.heap[1] = self.heap[self.size]
        self.size -= 1
        self.heap.pop()
        self.sift_down(1)
        return res

    def sift_up(self, i):
        if i == 1:
            return

        parent = i // 2
        if self.heap[parent] < self.heap[i]:
            self.heap[parent], self.heap[i] = self.heap[i], self.heap[parent]
            self.sift_up(parent)

    def sift_down(self, i):
        left = i * 2
        right = i * 2 + 1

        if left > self.size:
            return

        if right <= self.size and self.heap[left] < self.heap[right]:
            biggest = right
        else:
            biggest = left

        if self.heap[i] < self.heap[biggest]:
            self.heap[biggest], self.heap[i] = self.heap[i], self.heap[biggest]
            self.sift_down(biggest)

    def __repr__(self):
        return str(self.heap)

    def __len__(self):
        return self.size


def add(v):
    not_processed.remove(v)

    for vertex, weight in vertexes.get(v, dict()).items():
        if vertex in not_processed:
            mx_heap.add([weight, vertex])


def find_max_ost():
    add(1)
    ans = 0

    while len(mx_heap) != 0 and len(not_processed) != 0:
        mx_weight, mx_vertex = mx_heap.pop_max()
        if mx_vertex in not_processed:
            ans += mx_weight
            add(mx_vertex)

    if len(not_processed) != 0:
        print('Oops! I did it again')
        return
    print(ans)


def make_graph(e: int) -> dict:
    graph = dict()
    for _ in range(e):
        v, w, weight = map(int, input().split())
        if v not in graph:
            graph[v] = dict()

        if w not in graph:
            graph[w] = dict()

        graph[v][w] = max(graph[v].get(w, 0), weight)
        graph[w][v] = max(graph[w].get(v, 0), weight)

    return graph


n, m = map(int, input().split())
vertexes: dict = make_graph(m)

not_processed = {i for i in range(1, n + 1)}

mx_heap = MaxHeap()

find_max_ost()
