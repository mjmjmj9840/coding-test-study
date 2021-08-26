from collections import deque

N, M = map(int, input().split())
# 얼음 틀 입력 받기
graph = [list(input()) for _ in range(N)]
# 상 하 좌 우
moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs(x, y):
  queue = deque([(x, y)])
  graph[x][y] = '1'

  while queue:
    vx, vy = queue.popleft()
    for move in moves:
      ax = vx + move[0]
      ay = vy + move[1]
      if 0 <= ax < N and 0 <= ay < M and graph[ax][ay] == '0':
        queue.append((ax, ay))
        graph[ax][ay] = '1'

answer = 0
for i in range(N):
  for j in range(M):
    if graph[i][j] == '0':
      bfs(i, j)
      answer += 1

print(answer)
