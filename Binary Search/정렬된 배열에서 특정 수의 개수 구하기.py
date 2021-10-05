import sys
from bisect import bisect_left, bisect_right
input = sys.stdin.readline

n, x = map(int, input().split())
data = list(map(int, input().split()))
result = bisect_right(data, x) - bisect_left(data, x)  # x의 개수 세기

if result == 0:
    print(-1)
else:
    print(result)