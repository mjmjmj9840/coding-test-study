# 1509번: 팰린드롬 분할

s = input()
n = len(s)

# palindrome[i][j]: 문자열 i부터 j까지가 팰린드롬인지
palindrome = [[False] * n for _ in range(n)]

for i in range(n):
    palindrome[i][i] = True
    # 옆에 문자와 같다면 팰린드롬
    if i < n - 1 and s[i] == s[i + 1]:
        palindrome[i][i + 1] = True

for d in range(2, n):
    for i in range(n - d):
        j = i + d
        if s[i] == s[j] and palindrome[i + 1][j - 1]:
            palindrome[i][j] = True

# dp[i]: 문자열의 시작부터 i번째까지 최소 팰린드롬 개수
dp = [2501] * n
dp.append(0)

for i in range(n):
    for j in range(i, n):
        if palindrome[i][j]:
            dp[j] = min(dp[j], dp[i - 1] + 1)

print(dp[n - 1])
