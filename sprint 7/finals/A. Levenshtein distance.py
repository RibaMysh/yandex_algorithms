"""

ПРИНЦИП РАБОТЫ

Принцип работы алгоритма заключается в использовании динамического программирования
и разбиении задачи на более маленькие подзадачи.
Когда мы решаем задачу с использованием ДП, нужно ответить на 5 вопросов:

1. Что будет храниться в массиве dp?
   - В dp[i] (prev) будет храниться количество атомарных изменений для префиксов A[1:i].
   (Будем иметь в виду, что первый элемент строки A — это A[1], а A[0] = "").

2. Каким будет базовый случай для этой задачи?
   - Базовым случаем является ситуация, когда один из префиксов — пустая строка.
   Чтобы из пустой строки получить строку s длины n, нужно сделать n преобразований (добавить все буквы из s).

3. Каким будет переход динамики?
   - Переход динамики будет следующим:
     Если A[i] == B[j], то current[j] = dp[j - 1]
     (отбрасываем по последнему символу из каждой строки и рассматриваем новые префиксы).

     Если последние символы не одинаковые, то строки мы можем получить тремя преобразованиями.
     Возьмем минимум из префиксов, из которых мы можем получить нужную строку, а также сделаем +1,
     так как в любом случае будет выполнено хотя бы одно из трех действий:
     current[j] = 1 + min(prev[j], prev[j - 1], current[j - 1])

4. Каким будет порядок вычисления данных в массиве dp?
   - Будем "наращивать" поочередно строки, тем самым рассмотрим все варианты.

5. Где будет располагаться ответ на исходный вопрос?
   - Так как нас интересует ответ на вопрос, сколько нужно сделать преобразований, чтобы получить строку B из строки A,
     то ответ будет располагаться в последней ячейке, когда префиксы совпадают с исходными словами.

ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ

1. На вход программа получает две строки A и B.
2. На каждом этапе работы программы алгоритм обрабатывает отдельно взятый префикс строк A и B.
3. Программа заканчивает свою работу, когда все возможные префиксы были обработаны, и возвращает ответ.

ВРЕМЕННАЯ СЛОЖНОСТЬ

Пусть n — длина строки A, m — длина строки B.

Затраченная память:
   Все, что нам нужно хранить, — это два массива длинны n, один для текущего значения строки, другой для предыдущего.
   Затраченная память O(2n) => O(n).

Затраченное время:
   Так как мы проходим по всем возможным префиксам, то и затраченное время будет O(n * m).

"""


# id: 127499527

def solution(A, B):
    ln_a = len(A)
    ln_b = len(B)

    prev = [i for i in range(ln_a + 1)]

    for i in range(1, ln_b + 1):
        current = [i for i in range(ln_a + 1)]
        for j in range(ln_a + 1):
            if A[j - 1] == B[i - 1]:
                current[j] = prev[j - 1]
            else:
                current[j] = 1 + min(prev[j], prev[j - 1], current[j - 1])

        prev = current

    return prev[-1]


s = input()
t = input()
print(solution(s, t))
