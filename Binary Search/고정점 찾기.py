import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))

# 이진 탐색
start = 0
end = n - 1
while start <= end:
    idx = (start + end) // 2
    # 인덱스가 값보다 작은 경우 idx보다 작은쪽 탐색
    if idx < data[idx]:
        end = idx
    # 인덱스가 값보다 큰 경우 idx보다 큰쪽 탐색
    elif idx > data[idx]:
        start = idx
    # 고정점을 찾은 경우
    else:
        print(idx)
        break

# 고정점이 없는 경우
if start > end:
    print(-1)