n = int(input())
# dp[i][j]: (i, j)까지의 정수 합의 최댓값
dp = [[-1] * n for _ in range(n)]
for i in range(n):
	data = list(map(int, input().split()))
	for j in range(len(data)):
		dp[i][j] = data[j]

for i in range(1, n):
	for j in range(n):
		before = 0  # 이전 행까지의 최댓값
		# 왼쪽 위에서 오는 경우
		if j >= 1:
			before = dp[i - 1][j - 1]
		# 위에서 오는 경우
		before = max(before, dp[i - 1][j])
		
		dp[i][j] = dp[i][j] + before

print(max(dp[n - 1]))