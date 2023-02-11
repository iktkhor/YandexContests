import random

ls = list(map(int, input().split()))
N = ls[0]
K = ls[1]
M = ls[2]
ans = 0

if K >= M:
    while N >= K:
        zagotovki = N // K
        N -= zagotovki * K
        detali = K // M
        N += zagotovki * (K - detali * M)
        ans += detali * zagotovki

print(ans)
