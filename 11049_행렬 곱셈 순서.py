n = int(input())
p = [tuple(map(int, input().split())) for _ in range(n)]

dp = [[0] * n for _ in range(n)]
for diagonal in range(n - 1):
    for i in range(n - 1 - diagonal):
        j = i + diagonal + 1
        dp[i][j] = 2 ** 31
        for k in range(i, j):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j] + p[i][0] * p[k][1] * p[j][1])

print(dp[0][n - 1])
