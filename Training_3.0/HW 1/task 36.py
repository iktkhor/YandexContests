from collections import deque


def bfs(graph, used, start, target):
    if start == target:
        return 0

    que = deque()
    way_steps = 0
    que.append(start)
    used[start] = 0
    while que:
        length = len(que)
        way_steps += 1
        for _ in range(length):
            front_vertex = que.popleft()
            for to in graph[front_vertex]:
                if used[to] == -1:
                    used[to] = way_steps
                    que.append(to)
    return used[target]


v = int(input())
graph = [[] for i in range(v + 1)]
used = [-1 for i in range(v + 1)]

for i in range(v):
    line = list(map(int, input().split()))
    for j, el in enumerate(line, start=0):
        if el == 1:
            graph[i + 1].append(j + 1)

start, end = list(map(int, input().split()))
ans = bfs(graph, used, start, end)

if ans is not None:
    print(ans)
else:
    print(-1)

print(used)
