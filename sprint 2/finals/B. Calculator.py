"""

ПРИНЦИП РАБОТЫ
Весь алгоритм работает на одном стеке. Если честно, не особо понимаю, что описывать,
потому что я просто понял и делал по инструкции из задания.

ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ

1) Алгоритм на вход получает строку, состоящую из цифр, пробелов и знаков '+-/*'.
На выходе мы должны получить число — посчитанную по определенному принципу строку.

2) Так как нам сказано, что входные данные корректны, то всего есть 2 состояния работы.
1. Получили число — пушим его в стек.
2. Получили оператор — производим операцию над двумя ближайшими числами и записываем результат на вершину стека.
 Таким образом, у нас всегда на вершине стека будет лежать число — результат вычислений на текущем шаге.

3) Так как мы уже выяснили, что на вершине стека лежит нужное нам число,
 следовательно, после обработки всех входных данных, нам просто нужно вывести это число,
 и оно как раз будет тем, что нам нужно.

ВРЕМЕННАЯ СЛОЖНОСТЬ
n — длина входящей строки.
Затраченная память — O(n) на хранение строки и O(n) на стек. Амортизированная сложность — O(n).
Затраченное время на исполнение функций: split — O(n), проход по строке еще раз — O(n), len — O(n), isdigit — O(n),
все функции стека — константное время.
Хоть и так много функций от O(n), по факту мы проходим строку дважды, следовательно: O(n) + O(n) = O(2n) => O(n).


"""

# id: 115878244
from operator import add, sub, mul, floordiv


class StackException(Exception):
    pass


class Stack:
    def __init__(self):
        self.items = [None] * 2
        self.size = 0
        self.capacity = 2
        self.tail = 0

    def is_empty(self):
        return self.size == 0

    def error(self):
        if self.is_empty():
            raise StackException('Stack is empty')

    def check_capacity(self):
        if self.size == self.capacity:
            new_list = [None] * self.capacity
            self.items.extend(new_list)
            self.capacity *= 2

    def push(self, qwer):
        self.check_capacity()
        self.items[self.tail] = qwer
        self.tail += 1
        self.size += 1

    def pop(self) -> object:
        self.error()

        self.tail -= 1
        item = self.items[self.tail]
        self.items[self.tail] = None
        self.size -= 1
        return item

    def peek(self):
        self.error()
        return self.items[self.tail - 1]

    def __len__(self):
        return self.size

    def __str__(self):
        return str(self.items[:self.size])


stack = Stack()
commands = {'+': add, '-': sub, '*': mul, '/': floordiv}
#commands = {'+': op.add, '-': op.sub, '*': op.mul, '/': op.floordiv}
#в яндекс контесте такое решение работает дольше и занимает больше память, чем решение выше.
#объясните, пожалуйста, почему так ?
line = input().split()
for el in line:
    if len(el) > 1 or el.isdigit():
        stack.push(int(el))
    else:
        right = stack.pop()
        left = stack.pop()
        num = commands[el](left, right)
        stack.push(num)
print(stack.pop())