class Stack:
    def __init__(self):
        self.items = []
        self.max = []

    def push(self, item):
        self.items.append(item)
        if not self.max or item > self.max[-1]:
            self.max.append(item)
        else:
            self.max.append(self.max[-1])

    def pop(self):
        try:
            self.items.pop()
            self.max.pop()
        except IndexError:
            print("error")

    def get_max(self):
        try:
            print(self.max[-1])
        except IndexError:
            print("None")


stack = Stack()
for _ in range(int(input())):
    lst = input().split()
    if len(lst) == 2:
        command, value = lst
        getattr(stack, command)(int(value))
    else:
        command = lst[0]
        getattr(stack, command)()
