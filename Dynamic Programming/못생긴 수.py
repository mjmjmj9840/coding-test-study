n = int(input())

ugly = [0] * n  # 못생긴 수 리스트
ugly[0] = 1  # 1은 못생긴 수로 가정

# 2, 3, 5배 인덱스
i2 = i3 = i5 = 0
# 2, 3, 5 곱셈값
next2, next3, next5 = 2, 3, 5

# n번째까지의 못생긴 수 찾기
for i in range(1, n):
    ugly[i] = min(next2, next3, next5)
    # 인덱스에 따라서 곱셈값 증가
    if ugly[i] == next2:
        i2 += 1
        next2 = ugly[i2] * 2
    if ugly[i] == next3:
        i3 += 1
        next3 = ugly[i3] * 3
    if ugly[i] == next5:
        i5 += 1
        next5 = ugly[i5] * 5

print(ugly[n - 1])