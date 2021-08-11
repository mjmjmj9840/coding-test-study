# 2293번: 동전 1

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
dp = [0] * (k + 1)
dp[0] = 1

for coin in coins:
    for i in range(0, k + 1):
        if i + coin > k:
            break
        dp[i + coin] += dp[i]

print(dp[k])
