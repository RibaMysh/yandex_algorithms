def relax(v, w, weight, distance: list):
    if distance[v] + weight < distance[w]:
        distance[w] = distance[v] + weight


def find_min_vertex(distance, visited):
    mn = float('inf')
    vertex = -1
    for i in range(1, len(visited)):

        if not visited[i] and distance[i] < mn:
            mn = distance[i]
            vertex = i

    return vertex


def find_min_path(start, v):
    distance = [float('inf')] * (v + 1)
    distance[start] = 0

    visited = [False] * (v + 1)

    while True:
        current_vertex = find_min_vertex(distance, visited)

        if current_vertex == -1:
            break

        visited[current_vertex] = True

        if current_vertex in graphs:

            current_dict = graphs[current_vertex]

            for w, weight in current_dict.items():
                relax(current_vertex, w, weight, distance)

    for d in distance[1:]:
        print(-1 if d == float('inf') else d, end=' ')
    print()


def make_graph(e: int) -> dict:
    ans = dict()
    for _ in range(e):
        v, w, weight = map(int, input().split())

        if v not in ans:
            ans[v] = dict()

        if w not in ans:
            ans[w] = dict()

        ans[v][w] = min(
            ans[v].get(w, float('inf')), weight
        )

        ans[w][v] = min(
            ans[w].get(v, float('inf')), weight
        )

    return ans


n, m = map(int, input().split())
graphs = make_graph(m)

for i in range(1, n + 1):
    find_min_path(i, n)
