_input = input()
x = int(_input[1])
y = ord(_input[0]) - ord('a') + 1

moves = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, 2), (1, 2), (-1, -2), (1, -2)]
answer = 0

for move in moves:
  nx = x + move[0]
  ny = y + move[1]
  if 1 <= nx <= 8 and 1 <= ny <= 8:
    answer += 1

print(answer)
