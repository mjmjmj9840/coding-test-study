N, M = map(int, input().split())
data = [int(input()) for _ in range(N)]

dp = [10001] * (M + 1)
dp[0] = 0

for i in range(N):
    for j in range(data[i], M + 1):
        dp[j] = min(dp[j], dp[j - data[i]] + 1)

if dp[M] == 10001:
    print(-1)
else:
    print(dp[M])
