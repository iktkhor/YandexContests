def dfs(graph, visited, v, prev):
    visited[v] = 1
    global flag
    for to in graph[v]:
        if to != prev:
            if visited[to] == 0:
                dfs(graph, visited, to, v)
            elif visited[to] == 1 and flag:
                flag = False
    visited[v] = 2
    stack_way.append(v)


v, e = list(map(int, input().split()))
graph = [[] for i in range(v + 1)]
visited = [0 for i in range(v + 1)]
stack_way = []
flag = True

for i in range(e):
    pair = list(map(int, input().split()))
    graph[pair[0]].append(pair[1])

for i in range(1, len(visited)):
    if visited[i] == 0 and flag:
        dfs(graph, visited, i, 0)

if flag:
    print(' '.join(map(str, reversed(stack_way))))
else:
    print(-1)
