# 18405번: 경쟁적 전염

import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())
graph = []  # 시험관 정보
data = []  # 바이러스 정보
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
    input_ = list(map(int, input().split()))
    graph.append(input_)
    for j in range(n):
        if input_[j] != 0:
            # 바이러스 번호, 시간, x좌표, y좌표
            data.append((input_[j], 0, i, j))

target_s, target_x, target_y = map(int, input().split())

data.sort()  # 낮은 번호의 바이러스부터 처리하기 위해 정렬
queue = deque(data)

# BFS 수행
while queue:
    virus, s, x, y = queue.popleft()
    if s == target_s:
        break

    # 상하좌우 이동
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if graph[nx][ny] == 0:
                queue.append((virus, s + 1, nx, ny))
                graph[nx][ny] = virus

print(graph[target_x - 1][target_y - 1])
