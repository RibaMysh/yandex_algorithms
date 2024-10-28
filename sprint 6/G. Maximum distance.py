from queue import Queue


def make_graph(e: int) -> dict:
    ans = dict()
    for i in range(e):
        v, w = map(int, input().split())

        if v in ans:
            ans[v].append(w)
        else:
            ans[v] = [w]

        if w in ans:
            ans[w].append(v)
        else:
            ans[w] = [v]

    for value in ans.values():
        value.sort()

    return ans


def bfs(start):
    planned = Queue()
    planned.put(start)
    colors[start] = 'g'
    while not planned.empty():
        v = planned.get()

        for w in graphs.get(v, []):
            if colors[w] == 'w':
                colors[w] = 'g'
                distance[w] = distance[v] + 1
                planned.put(w)
        colors[v] = 'b'


n, m = map(int, input().split())
graphs = make_graph(m)
s = int(input())

colors = ['w'] * (n + 1)
distance = [-1] * (n + 1)
distance[s] = 0
bfs(s)
print(max(distance))
