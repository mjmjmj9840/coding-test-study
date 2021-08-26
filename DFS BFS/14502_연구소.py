# 14502번: 연구소

import copy
from itertools import combinations

n, m = map(int, input().split())
graph = []
empty = []
virus = []
temp = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 지도 정보 입력 받기
for i in range(n):
    data = list(map(int, input().split()))
    graph.append(data)
    for j in range(m):
        if data[j] == 0:
            empty.append((i, j))
        elif data[j] == 2:
            virus.append((i, j))

# 바이러스 전파
def dfs(i, j):
    global count
    # 상하좌우 이동
    for k in range(4):
        nx, ny = i + dx[k], j + dy[k]
        if 0 <= nx < n and 0 <= ny < m:
            if temp[nx][ny] == 0:
                temp[nx][ny] = 2
                count += 1
                dfs(nx, ny)


# 빈 칸을 3개 고르는 경우의 수
candidates = list(combinations(empty, 3))
result = 0

for a, b, c in candidates:
    temp = copy.deepcopy(graph)  # 벽을 세운 경우 가정
    # 벽 세우기
    temp[a[0]][a[1]] = 1
    temp[b[0]][b[1]] = 1
    temp[c[0]][c[1]] = 1
    count = 0  # 감염된 칸의 수

    # 모든 바이러스 좌표에 대해 dfs 실행
    for i, j in virus:
        dfs(i, j)

    result = max(result, len(empty) - count - 3)  # 안전 영역 크기의 최댓값

print(result)
