ls = ls = list(map(int, input().split()))
flag = True

for i in range(len(ls) - 1):
    if ls[i] >= ls[i + 1]:
        flag = False
        break

if flag:
    print("YES")
else:
    print("NO")