def make_graphs(e: int):
    ret = dict()
    for _ in range(e):
        v, w = map(int, input().split())
        lst: list = ret.get(v, [])
        lst.append(w)
        ret[v] = lst

    for val in ret.values():
        val.sort(reverse=True)

    return ret


def dfs(s: int):
    timer = -1
    stack = list()
    stack.append(s)

    while stack:

        v: int = stack.pop()
        if colors[v] != 'b':
            timer += 1

        if colors[v] == 'w':

            ent[v] = timer
            colors[v] = 'g'
            stack.append(v)

            for w in graphs.get(v, []):
                if colors[w] == 'w':
                    stack.append(w)

        elif colors[v] == 'g':
            colors[v] = 'b'
            leave[v] = timer


n, m = map(int, input().split())

colors = ['w'] * (n + 1)
ent = [-1] * (n + 1)
leave = [-1] * (n + 1)

graphs = make_graphs(m)
dfs(1)
for i in range(1, n + 1):
    print(ent[i], leave[i])
