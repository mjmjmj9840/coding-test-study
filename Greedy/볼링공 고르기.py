# 볼링공 고르기
n, m = map(int, input().split())
data = list(map(int, input().split()))
data.sort()

count = 1
result = 0
for i in range(1, n):
    if data[i - 1] == data[i]:
        count += 1
    else:
        result += (count * (n - i))
        count = 1
    # 최대 무게일 경우 중지
    if data[i] == m:
        break

print(result)
