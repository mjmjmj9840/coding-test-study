# 22252번: 정보 상인 호석

from collections import defaultdict
import heapq
import sys

input = sys.stdin.readline
dict = defaultdict(list)

q = int(input())
result = 0

for _ in range(q):
    data = input().split()
    op = int(data[0])
    name = data[1]
    k = int(data[2])

    if op == 1:  # 고릴라가 정보를 얻음
        for i in range(k):
            # 최대 힙을 이용한 내림차순 heapsort
            heapq.heappush(dict[name], -int(data[i + 3]))
    elif op == 2:  # 호석이가 정보를 삼
        if k >= len(dict[name]):  # 모든 정보 사기
            k = len(dict[name])

        for i in range(k):  # k개의 정보 사기
            result += -heapq.heappop(dict[name])

print(result)
