str1 = '0' + input()
str2 = '0' + input()
dp = [[0] * (len(str2)) for _ in range(len(str1))]

for i in range(1, len(str1)):
    for j in range(1, len(str2)):
        if str1[i] == str2[j]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

i = len(str1) - 1
j = len(str2) - 1
result = ''

while dp[i][j] > 0:
    if dp[i][j - 1] == dp[i][j]:
        j -= 1  # 위쪽으로 이동
    elif dp[i - 1][j] == dp[i][j]:
        i -= 1  # 왼쪽으로 이동
    else:
        result += str1[i]
        i -= 1  # 대각선으로 이동
        j -= 1

print(dp[-1][-1])
if len(result) > 0:
    print(result[::-1])
