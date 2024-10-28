def make_graph(m: int) -> dict:
    ans = dict()
    for i in range(m):
        v, w = map(int, input().split())
        lst = ans.get(v, [])
        lst.append(w)
        ans[v] = lst
    return ans


def sort_dfs():
    ans = []
    for v in range(1, len(colors)):
        if colors[v] == 'w':
            dfs(v, ans)
    print(*ans[::-1])


def dfs(v: int, ans):
    stack = list()
    stack.append(v)
    while stack:

        v = stack.pop()

        if colors[v] == 'w':
            colors[v] = 'g'
            stack.append(v)

            for w in graphs.get(v, []):
                if colors[w] == 'w':
                    stack.append(w)

        elif colors[v] == 'g':
            colors[v] = 'b'
            ans.append(v)


n, m = map(int, input().split())
graphs = make_graph(m)

colors = ['w'] * (n + 1)
sort_dfs()
