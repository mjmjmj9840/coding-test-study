# 1213번: 팰린드롬 만들기

name = input()
alphabet = [0] * 26  # 알파벳 개수 세기

for c in name:
    i = ord(c) - ord('A')
    alphabet[i] += 1

result = ''  # 팰린드롬의 앞부분 절반
middle = ''  # 팰린드롬의 정가운데 문자
possible = True
for i in range(26):
    cnt = alphabet[i]
    if cnt % 2 == 1:
        if middle == '':
            middle = chr(i + ord('A'))
        else:  # 팰린드롬을 만들 수 없는 경우
            possible = False
            break
    if cnt > 0:
        result += chr(i + ord('A')) * (cnt // 2)

if possible:
    print(result + middle + result[::-1])
else:
    print("I'm Sorry Hansoo")
