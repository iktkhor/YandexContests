from collections import deque


def get_cicle(stack, ans, target):
    while stack[-1] != target:
        if stack[-1] not in ans:
            ans.append(stack[-1])
        stack.pop()
    ans.append(stack[-1])


def dfs(graph, visited, v):
    stack_way.append(v)
    visited[v] = 1
    for to in graph[v]:
        if visited[to] == 0:
            dfs(graph, visited, to)
        elif visited[to] == 1 and not ans:
            get_cicle(stack_way.copy(), ans, to)
    visited[v] = 2
    stack_way.pop()


# v = int(input())
students, pairs = list(map(int, input().split()))
graph = [[] for i in range(students + 1)]
visited = [0] * (students + 1)
stack_way = deque()
ans = []
count = 0

# for i in range(v):
#     line = list(map(int, input().split()))
#     for j, el in enumerate(line, start=0):
#         if el == 1:
#             graph[i + 1].append(j + 1)

for i in range(pairs):
    pair = list(map(int, input().split()))
    graph[pair[0]].append(pair[1])
    #graph[pair[1]].append(pair[0])
#print(graph)

for i in range(1, len(visited)):
    if visited[i] == 0 and not ans:
        dfs(graph, visited, i)
#print(visited)

if ans:
    print('YES')
    # print(len(ans))
    print(' '.join(map(str, reversed(ans))))
else:
    print('NO')
