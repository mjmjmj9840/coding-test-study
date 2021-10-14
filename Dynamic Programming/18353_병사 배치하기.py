n = int(input())
array = list(map(int, input().split()))
# dp[i]: i번째까지의 남아있는 최대 병사의 수
dp = [1] * n

for i in range(1, n):
    for j in range(0, i):
        # 내림차순을 만족하는 원소에 대해 dp 갱신
        if array[j] > array[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))