X = int(input())
dp = [0] * (X + 1)

for i in range(2, X + 1):
    count = 987654321
    if i % 5 == 0:
        count = min(count, dp[i // 5] + 1)
    if i % 3 == 0:
        count = min(count, dp[i // 3] + 1)
    if i % 2 == 0:
        count = min(count, dp[i // 2] + 1)

    dp[i] = min(count, dp[i - 1] + 1)

print(dp[X])
