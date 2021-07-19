s = input()
count = {'0': 0, '1': 0}  # 문자열에서 연속된 숫자가 나오는 횟수
before = s[0]
count[s[0]] += 1

for i in range(1, len(s)):
    # 연속된 숫자가 끝날 때
    if s[i] != before:
        count[s[i]] += 1
        before = s[i]

print(min(count.values()))
