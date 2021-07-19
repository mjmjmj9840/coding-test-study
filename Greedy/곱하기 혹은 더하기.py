s = list(map(int, input()))
answer = s[0]

for i in range(1, len(s)):
    # 두 항 중 하나라도 1 이하일 경우 덧셈
    if answer <= 1 or s[i] <= 1:
        answer += s[i]
    # 그 외에는 곱셈
    else:
        answer *= s[i]

print(answer)
