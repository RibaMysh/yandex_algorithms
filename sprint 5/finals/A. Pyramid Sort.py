"""

ПРИНЦИП РАБОТЫ

Принцип работы алгоритма пирамидальной сортировки можно разбить на два этапа:
1. Создание корректной кучи.
2. Удаление корня с поддержанием свойства кучи.

ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ

1. На вход программа получает в первой строке число n, затем в n строках идут участники в виде:
    <уникальный логин> <число решённых задач> <штраф>.
   Уникальный логин — строка из маленьких латинских букв длиной не более 20 символов; число задач, штраф — целые числа.

2. На каждом этапе работы алгоритм выводит "максимального" пользователя,
удаляя его из кучи, и восстанавливает свойства кучи.

3. Алгоритм прекращает свою работу после вывода всех участников.

ВРЕМЕННАЯ СЛОЖНОСТЬ

Пусть n — длина входного массива.

Затраченная память:
Память — O(1), так как в данной реализации элементы поочередно выводятся в порядке убывания.
(Можно было бы переделать алгоритм так, чтобы максимальные элементы записывались в конец массива,
а после завершения сортировки массив был перевернут и возвращен.
Однако даже в этом случае память остаётся O(1), так как алгоритм работает с исходным массивом.)

Затраченное время:
В начале алгоритм строит корректную кучу на максимум за O(n)
(Я не могу доказать это самостоятельно, так как до конца не понимаю, как это работает,
но вот ссылка на ресурс, где я нашел информацию:
https://neerc.ifmo.ru/wiki/index.php?title=Двоичная_куча).

После построения кучи алгоритм n раз применяет функцию sift_down,
которая, как известно из курса, работает за O(log n). Следовательно, сама сортировка выполняется за O(n log n).

Итого: построение кучи занимает O(n), а сортировка — O(n log n). Время работы алгоритма: O(n log n).
"""

# id: 120105427

from functools import total_ordering


def swap(arr, left, right):
    arr[left], arr[right] = arr[right], arr[left]


@total_ordering
class Person:
    def __init__(self, login, value, fine):
        self.log = login
        self.value = value
        self.fine = fine

    def __lt__(self, other):
        if self.value != other.value:
            return self.value < other.value

        if self.fine != other.fine:
            return self.fine > other.fine

        return self.log > other.log

    def __eq__(self, other):
        if self.value != other.value or self.fine != other.fine or self.log != other.log:
            return False
        return True

    def __repr__(self):
        return self.log


class Heap:
    def __init__(self, arr):
        self.size = len(arr) - 1
        self.arr = self.make_heap(arr)

    def make_heap(self, arr: list) -> list:
        for index in range(len(arr) // 2 + 1, 0, -1):
            self.sift_down(arr, index)
        return arr

    def sift_down(self, arr, index):
        left = 2 * index
        right = 2 * index + 1

        if left > self.size:
            return

        if right <= self.size and arr[right] > arr[left]:
            largest = right
        else:
            largest = left

        if arr[largest] > arr[index]:
            swap(arr, index, largest)
            self.sift_down(arr, largest)

    def heap_sort(self):
        while self.size > 0:
            print(self.pop_max())

    def pop_max(self):
        res = self.arr[1]
        self.arr[1] = self.arr[self.size]
        self.size -= 1
        self.sift_down(self.arr, 1)
        return res


n = int(input())
peoples = [None]
for i in range(n):
    log, val, f = input().split()
    peoples.append(Person(log, int(val), int(f)))
h = Heap(peoples)
h.heap_sort()
