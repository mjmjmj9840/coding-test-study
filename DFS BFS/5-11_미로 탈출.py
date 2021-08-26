from collections import deque

N, M = map(int, input().split())
# 2차원 미로 정보 입력 받기: 괴물 있음 0/괴물 없음 1
graph = [list(map(int, input())) for _ in range(N)]
# 이동할 방향(상 하 좌 우)
moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# BFS로 최단 거리 찾기
queue = deque([(0, 0)])
while queue:
  x, y = queue.popleft()

  for move in moves:
    vx = x + move[0]
    vy = y + move[1]
    if 0 <= vx < N and 0 <= vy < M and graph[vx][vy] == 1:
      queue.append((vx, vy))
      graph[vx][vy] = graph[x][y] + 1

print(graph[N - 1][M - 1])
