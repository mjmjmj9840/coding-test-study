# 2110번: 공유기 설치
import sys

input = sys.stdin.readline

n, c = map(int, input().split())
array = [int(input()) for _ in range(n)]
array.sort()
result = 0

start = 1
end = (array[0] + array[-1]) // (c - 1)

while start <= end:
    mid = (start + end) // 2

    previous = array[0]  # 이전에 공유기를 설치한 위치
    count = 2  # 현재 설치한 공유기의 개수(처음과 끝)
    for i in range(1, n - 1):
        if count == c:
            break
        if array[i] - previous >= mid:
            # 공유기 설치
            previous = array[i]
            count += 1

    # 모든 공유기 사이의 거리가 mid 이상인 경우
    if count == c and array[-1] - previous >= mid:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)
