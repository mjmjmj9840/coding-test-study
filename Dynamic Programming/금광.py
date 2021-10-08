T = int(input())

while T:
	n, m = map(int, input().split())
	data = list(map(int, input().split()))
	array = [[data[i * m + j] for j in range(m)] for i in range(n)]
	# dp[i][j]: array[i][j]까지의 채굴할 수 있는 금의 최댓값
	dp = [[0] * m for _ in range(n)]
	for i in range(n):
		dp[i][0] = array[i][0]
	
	for j in range(1, m):
		for i in range(n):
			for k in range(i - 1, i + 2):
				# 범위를 벗어나지 않는 경우 최댓값 갱신
				if 0 <= k < n:
					dp[i][j] = max(dp[i][j], array[i][j] + dp[k][j - 1])
	
	# 채굴할 수 있는 금의 최대값 구하기
	result = 0
	for i in range(n):
		result = max(result, dp[i][m - 1])

	print(result)
	T -= 1