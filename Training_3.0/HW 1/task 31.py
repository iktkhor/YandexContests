def dfs(graph, visited, v):
    visited[v] = 1
    for to in graph[v]:
        if visited[to] == 0:
            dfs(graph, visited, to)


v, edges = list(map(int, input().split()))
graph = [[] for i in range(v + 1)]
visited = [0] * (v + 1)
for i in range(edges):
    dots = list(map(int, input().split()))
    graph[dots[0]].append(dots[1])
    graph[dots[1]].append(dots[0])
    print(i, dots[0], dots[1])
dfs(graph, visited, 1)

count = 0
comp = []
for i in range(1, v + 1):
    if visited[i] == 1:
        count += 1
        comp.append(i)

print(count)
print(' '.join(map(str, sorted(comp))))
