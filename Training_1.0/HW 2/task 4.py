ls = list(map(int, input().split()))
ans = 0

for i in range(1, len(ls) - 1):
    if ls[i] > ls[i - 1] and ls[i] > ls[i + 1]:
        ans += 1

print(ans)
