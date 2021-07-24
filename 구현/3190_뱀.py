# 3190번: 뱀

from collections import deque

n = int(input())  # 보드의 크기
board = [[0] * (n + 1) for _ in range(n + 1)]

k = int(input())  # 사과의 개수
for _ in range(k):  # 사과 위치를 2로 표현
  x, y = map(int, input().split())
  board[x][y] = 2
  
l = int(input())  # 뱀의 방향 전환 횟수
moves = deque([])  # 뱀의 방향 전환 정보
for _ in range(l):
  x, c = input().split()
  moves.append((int(x), c))

# 상, 우, 하, 좌 방향 표현
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
head = [1, 1]  # 뱀의 머리 좌표
body = deque([(1, 1)])  # 뱀의 몸이 위치한 좌표 리스트
board[1][1] = 1  # 뱀의 몸 위치를 1로 표현
d = 1  # 시작 방향(오른쪽)
t = 0  # 걸린 시간

while True:
  # 방향 변환이 있을 경우
  if moves and t == moves[0][0]:
    if moves[0][1] == 'L':
      d = (d - 1) % 4
    elif moves[0][1] == 'D':
      d = (d + 1) % 4
    moves.popleft()

  # 머리를 다음칸에 위치시킨다
  head[0] += directions[d][0]
  head[1] += directions[d][1]

  # 벽이나 자기자신의 몸과 부딪히면 게임 종료
  if head[0] < 1 or head[0] > n or head[1] < 1 or head[1] > n or board[head[0]][head[1]] == 1:
    print(t + 1)
    break

  # 사과가 없을 경우 뱀의 꼬리 앞으로 한 칸 이동
  if board[head[0]][head[1]] == 0:
    tail = body.popleft()
    board[tail[0]][tail[1]] = 0

  # 새로운 머리를 몸 좌표에 추가
  body.append((head[0], head[1]))
  board[head[0]][head[1]] = 1

  t += 1

  
