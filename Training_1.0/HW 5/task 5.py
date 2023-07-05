trees, sorts = list(map(int, input().split()))
set_sorts = {i + 1 for i in range(sorts)}
colors = list(map(int, input().split()))
min_diff = len(colors)
ans = ''

for i in range(trees):
    for j in range(i, trees):
        set_ = set()
        diff = j - i
        for k in range(i, j + 1):
            set_.add(colors[k])
        #print(set_)
        if set_sorts == set_ and diff < min_diff:
            min_diff = diff
            ans = f'{i + 1} {j + 1}'

print(ans)
