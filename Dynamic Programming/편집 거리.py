str1 = '0' + input()
str2 = '0' + input()
# str1과 str2의 최장 공통 부분 수열
dp = [[0] * (len(str2)) for _ in range(len(str1))]

for i in range(1, len(str1)):
    for j in range(1, len(str2)):
        if str1[i] == str2[j]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

cnt = abs(len(str1) - len(str2))  # 삽입/삭제해야하는 문자의 수
cnt += (len(str1) - 1) - dp[-1][-1]  # 교체해야하는 문자의 수
print(cnt)