# 15686번: 치킨 배달

from itertools import combinations

n, m = map(int, input().split())
house = []  # 집 정보
chicken = []  # 치킨집 정보

for i in range(n):
  data = list(map(int, input().split()))
  for j in range(n):
    if data[j] == 1:  # 집 정보 저장
      house.append((i, j))
    if data[j] == 2:  # 치킨집 정보 저장
      chicken.append((i, j))

# c_dist[i][j]: i번째 치킨집과 j번째 집의 치킨거리
c_dist = [[0] * len(house) for _ in range(len(chicken))]
for i in range(len(chicken)):
  for j in range(len(house)):
    c_dist[i][j] = abs(chicken[i][0] - house[j][0]) + abs(chicken[i][1] - house[j][1])

answer = 987654321  # 도시의 치킨거리
candidates = list(combinations([i for i in range(len(chicken))], m))
for x in candidates:
  result = [101] * len(house)  # 각 집의 최소 치킨거리
  for i in x:
    for j in range(len(house)):
      result[j] = min(result[j], c_dist[i][j])
  answer = min(answer, sum(result))

print(answer)
