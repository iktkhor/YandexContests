def dfs(graph, visited, v, prev):
    color = 3 - visited[prev]
    visited[v] = color
    for to in graph[v]:
        if to != prev:
            if visited[to] == 0:
                dfs(graph, visited, to, v)
            elif visited[to] == color:
                global flag
                flag = False


students, pairs = list(map(int, input().split()))
graph = [[] for i in range(students + 1)]
visited = [0] * (students + 1)
visited[0] = 2
flag = True

for i in range(pairs):
    pair = list(map(int, input().split()))
    graph[pair[0]].append(pair[1])
    graph[pair[1]].append(pair[0])
#print(graph)
#print(visited)
for i in range(1, len(visited)):
    if visited[i] == 0 and flag:
        dfs(graph, visited, i, 0)
#print(visited)
if flag:
    print('YES')
else:
    print('NO')
