def make_graphs_lst(m: int) -> dict:
    graphs = dict()
    for _ in range(m):
        v1, v2 = map(int, input().split())
        lst: list = graphs.get(v1, [])
        lst.append(v2)
        graphs[v1] = lst

        lst = graphs.get(v2, [])
        lst.append(v1)
        graphs[v2] = lst

    for key in graphs.keys():
        graphs[key].sort(reverse=True)

    return graphs


def dfs(v):
    stack = list()
    stack.append(v)
    while stack:
        v = stack.pop()

        if colors[v] == 'w':

            colors[v] = 'g'
            print(v, end=' ')
            stack.append(v)

            for w in graphs.get(v, []):
                if colors[w] == 'w':
                    stack.append(w)

        elif colors[v] == 'g':
            colors[v] = 'b'


n, m = map(int, input().split())
graphs = make_graphs_lst(m)

colors = ['w'] * (n + 1)

dfs(int(input()))
