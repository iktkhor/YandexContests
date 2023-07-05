def count_ways(cells, max_jump):
    dp = [0] * (cells + 1)
    dp[1] = 1
    for i in range(1, cells + 1):
        k = 1
        while k <= max_jump and i - k >= 0:
            dp[i] += dp[i - k]
            k += 1
    return dp[-1]


N, K = list(map(int, input().split()))
ans = count_ways(N, K)
print(ans)
