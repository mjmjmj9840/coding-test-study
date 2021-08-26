N = int(input())

data = []
for _ in range(N):
  name, score = input().split()
  data.append((name, int(score)))

data.sort(key = lambda x: x[1])

for name, score in data:
  print(name, end=' ')
