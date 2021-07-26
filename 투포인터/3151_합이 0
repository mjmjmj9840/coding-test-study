# 3151번: 합이 0

import sys
from collections import Counter

input = sys.stdin.readline
n = int(input())
data = list(map(int, input().split()))
data.sort()
cnt = Counter(data)  # data의 개수 저장
result = 0

for i in range(n - 2):
    if data[i] > 0:  # 세 수 중 하나는 반드시 음수여야 함
        break
    target = -data[i]  # 만들어야 하는 합
    lo = i + 1
    hi = n - 1

    while lo < hi:
        s = data[lo] + data[hi]
        if s < target:
            lo += 1  # 더 큰 수 더하기
        elif s > target:
            hi -= 1  # 더 작은 수 더하기
        else:  # s == target
            if data[lo] == data[hi]:  # 같은 수의 개수
                result += hi - lo
            else:  # 오른쪽 수의 개수
                result += cnt[data[hi]]
            lo += 1

print(result)
