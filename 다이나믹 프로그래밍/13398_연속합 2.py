# 13398번: 연속합 2
import sys

input = sys.stdin.readline
n = int(input())
data = list(map(int, input().split()))
data.insert(0, -1001)  # dp 테이블과 인덱스를 맞추기 위해
# dp[i][0]: i번째 원소를 삭제하지 않을 경우 i번째까지의 최대 부분합
# dp[i][1]: i번째 원소를 삭제할 경우 i번째까지의 최대 부분합
dp = [[0] * 2 for _ in range(n + 1)]
dp[0][0] = dp[0][1] = 0
max_sum = -1001

for i in range(1, n + 1):
    dp[i][0] = max(dp[i - 1][0] + data[i], data[i])
    dp[i][1] = max(dp[i - 1][0], dp[i - 1][1] + data[i])
    max_sum = max(max_sum, max(dp[i][0], dp[i][1]))

if max_sum == 0:
    print(max(data))
else:
    print(max_sum)
