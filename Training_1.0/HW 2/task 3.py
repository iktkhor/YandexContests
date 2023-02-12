N = int(input())
ls = list(map(int, input().split()))
x = int(input())
diff = abs(x - ls[0])
ans = ls[0]

for i in range(1, len(ls)):
    if abs(x - ls[i]) < diff:
        diff = abs(x - ls[i])
        ans = ls[i]

print(ans)

