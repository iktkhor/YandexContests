def dfs(graph, visited, v):
    visited[v] = components
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

components = 0
for i in range(1, len(visited)):
    if visited[i] == 0:
        components += 1
        dfs(graph, visited, i)

print(components)
for i in range(1, components + 1):
    count = 0
    comp = []
    for j in range(len(visited)):
        if visited[j] == i:
            count += 1
            comp.append(j)
    print(count)
    print(' '.join(map(str, sorted(comp))))
