houses = int(input())
mean_cost = list(map(int, input().split()))
ans = [-1 for i in range(houses)]
stack = []

for i in range(houses):
    while len(stack) > 0 and stack[len(stack) - 1][0] > mean_cost[i]:
        ans[stack[len(stack) - 1][1]] = i
        stack.pop()
    stack.append([mean_cost[i], i])

print(' '.join(map(str, ans)))
