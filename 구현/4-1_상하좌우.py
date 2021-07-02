N = int(input())
plans = list(input().split())

directions = {"L": (0, -1), "R": (0, 1), "U": (-1, 0), "D": (1, 0)}
x, y = 1, 1

for plan in plans:
  direction = directions[plan]
  nx = x + direction[0]
  ny = y + direction[1]
  # NxN을 벗어날 경우 무시한다
  if nx < 1 or nx > N or ny < 1 or ny > N:
    continue
  x, y = nx, ny

print(x, y)
