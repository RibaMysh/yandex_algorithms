"""

**ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ**

1. В первой строке мы получаем число n (количество документов),
далее на n строках идут не пустые документы, состоящие из слов, разделенных пробелами.
На n+1-й строке указано число m (количество запросов),
на m строках идут m не пустых запросов, состоящих из слов, разделенных пробелами.

2. На каждом шаге программа обрабатывает запрос.
Из запроса берутся все уникальные слова, и по количеству их вхождений во все документы строится релевантность
для каждого документа.
После этого релевантности сортируются, и выводятся первые 5 ненулевых элементов самых релевантных документов.

3. Программа завершает свою работу после обработки всех запросов.

**ВРЕМЕННАЯ СЛОЖНОСТЬ**

Затраченная память:
На хранение счетчика в худшем случае потребуется O(1000n) -> O(n).
Для каждого запроса хранится массив длины O(n), который обнуляется при каждом новом запросе.

Временная сложность:
На создание счетчика в худшем случае уйдет O(1000n) -> O(n), так как вставка и проверка наличия в map работает за O(1).

Далее m раз повторяется функция find_index, разберем, сколько она занимает по времени.
На вход функция получает массив уникальных слов. Пусть q — число уникальных слов, тогда функция составит
релевантности за O(s) (опять же благодаря скорости работы таблицы),
но еще нужно отсортировать массив за O(n log n).
(Знающие люди рассказали мне про сортировку при помощи кучи, которая работает за O(n log k), где k — количество
первых элементов. Значит, можно было сделать все за O(n log 5) -> O(n), но я не знаю, где мне найти хорошее объяснение
этого алгоритма и структуры данных. Если вы знаете, где я могу посмотреть про это, то не могли бы вы, пожалуйста,
прикрепить в ревью ссылочку.)

Таким образом, программа работает за O(n) + O(m(n log n)) -> O(m(n log n)).

"""

# id: 118314822

from typing import List, Union


def find_top_5_elements(arr):
    top_5 = []

    for _ in range(5):
        max_element = None
        max_index = -1

        for i in range(len(arr)):
            if arr[i] != 0:
                if max_element is None or arr[i][0] > max_element[0] or (
                        arr[i][0] == max_element[0] and arr[i][1] < max_element[1]):
                    max_element = arr[i]
                    max_index = i

        if max_element is not None:
            top_5.append(max_element)
            arr[max_index] = 0

    return top_5


def find_index(requests: set, counter: dict, ln: int):
    ans: List[Union[int, List[int]]] \
        = [0] * (ln + 1)

    for word in requests:

        if word in counter:
            d = counter[word]

            for index, v in d.items():

                if ans[index] == 0:
                    ans[index] = [v, index]
                else:
                    ans[index][0] += v

    if ans:
        for a in find_top_5_elements(ans):
            print(a[1], end=' ')
        print()


n = int(input())
counter = dict()

for i in range(n):
    line = input().split()
    index = i + 1
    for word in line:
        if word not in counter:
            counter[word] = {index: 1}
        else:
            if index not in counter[word]:
                counter[word][index] = 1
            else:
                counter[word][index] += 1

m = int(input())

for _ in range(m):
    line = set(input().split())
    find_index(line, counter, n)
