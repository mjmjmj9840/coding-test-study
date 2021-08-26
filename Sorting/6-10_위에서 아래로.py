N = int(input())
array = []
for _ in range(N):
  array.append(int(input()))

array.sort(reverse=True)

for x in array:
  print(x, end = ' ')
