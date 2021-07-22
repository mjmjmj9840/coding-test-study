# 문자열 재정렬

s = input()
result = []
number = 0
for x in s:
    if x.isalpha():
        result.append(x)
    else:
        number += int(x)

result.sort()
if number != 0:
    result.append(str(number))

print(''.join(result))  # 리스트를 문자열로 변환
