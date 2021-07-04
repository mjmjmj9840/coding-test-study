N, M = map(int, input().split())
x, y, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# 북 동 남 서
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
arr[x][y] = 1
answer = 1
count = 0

while True:
  count += 1
  d = (d - 1) % 4
  nx = x + directions[d][0]
  ny = y + directions[d][1]
  # 앞이 육지일 경우 한 칸 전진
  if arr[nx][ny] == 0:
    x, y = nx, ny
    arr[x][y] = 1
    count = 0
    answer += 1
  # 네 방향 모두 이동할 수 없는 경우
  if count == 4:
    d = (d - 2) % 4
    nx = x + directions[d][0]
    ny = y + directions[d][1]
    # 뒤로 한 칸 가기
    if arr[nx][ny] == 0:
      x, y = nx, ny
      arr[x][y] = 1
      count = 0
    else:
      break

print(answer)
