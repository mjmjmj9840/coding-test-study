N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

answer = 0
for row in arr:
  answer = max(answer, min(row))

print(answer)
