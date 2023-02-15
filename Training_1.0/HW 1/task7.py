import random

N, K, M = list(map(int, input().split()))
ans = 0

if K >= M:
    while N >= K:
        zagotovki = N // K
        N -= zagotovki * K
        detali = K // M
        N += zagotovki * (K - detali * M)
        ans += detali * zagotovki

print(ans)
