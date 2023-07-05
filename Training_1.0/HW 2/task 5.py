n = int(input())
ls = list(map(int, input().split()))
throw = 0
ans = 0
max_throw = ls[0]

for i in range(len(ls)):
    if max_throw < ls[i]:
        max_throw = ls[i]

for i in range(1, len(ls) - 1):
    if ls[i] % 5 == 0 and ls[i] % 10 != 0 and ls[i - 1] == max_throw and ls[i + 1] < ls[i]:
        if ls[i] > throw:
            throw = ls[i]

if throw > 0:
    ans = 1
    for i in range(len(ls)):
        if ls[i] > throw:
            ans += 1

print(ans)
