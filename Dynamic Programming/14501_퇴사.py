n = int(input())
array = [tuple(map(int, input().split())) for _ in range(n)]
dp = [0] * (n + 1)  # i번째부터 마지막 날까지의 최대 수익 dp 테이블
max_value = 0

# 마지막날부터 거꾸로 계산
for i in range(n - 1, -1, -1):
    fin = i + array[i][0]  # 상담이 끝나는 날
    if fin <= n:  # 기간 내에 상담 가능
        dp[i] = max(max_value, dp[fin] + array[i][1])
        max_value = max(max_value, dp[i])
    else:
        dp[i] = max_value

print(max_value)