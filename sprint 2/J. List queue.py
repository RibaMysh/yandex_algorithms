class Q:
    def __init__(self):
        self.values = []

    def get(self):
        if self.values:
            print(self.values[0])
            self.values = self.values[1:]

        else:
            print('error')

    def put(self, value):
        self.values.append(value)

    def size(self):
        print(len(self.values))


q = Q()
for i in range(int(input())):
    command = input()
    if command in ["get", "size"]:
        getattr(q, command)()
    else:
        q.put(int(command.split()[1]))
