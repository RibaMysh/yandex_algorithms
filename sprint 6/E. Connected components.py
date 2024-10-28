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

    return ans


def dfs(v, color, ans):
    stack = list()
    stack.append(v)

    while stack:
        v = stack.pop()
        if colors[v] == -1:
            colors[v] = color
            if color in ans:
                ans[color].append(v)
            else:
                ans[color] = [v]

            stack.append(v)
            for w in graphs.get(v, []):
                if colors[w] == -1:
                    stack.append(w)


def total_dfs():
    ans = dict()
    component_count = 1
    for v in range(1, len(colors)):
        if colors[v] == -1:
            dfs(v, component_count, ans)
            component_count += 1
    print(len(ans))
    for value in ans.values():
        print(*sorted(value))


n, m = map(int, input().split())
graphs = make_graph(m)

colors = [-1] * (n + 1)
total_dfs()
