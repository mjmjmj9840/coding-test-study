# 16234번: 인구 이동
from collections import deque

n, l, r = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# 하루동안 발생하는 인구 이동
def move():
    visited = [[False] * n for _ in range(n)]
    is_moved = False  # 인구 이동이 일어났는지
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                union, total_people = bfs(visited, i, j)
                # 연합에 속한 나라가 2개 이상일 경우
                if len(union) > 1:
                    each_people = total_people // len(union)  # 연합 내 각 나라의 인구수
                    # 연합 내 인구 이동
                    for x, y in union:
                        array[x][y] = each_people
                    is_moved = True

    return is_moved


def bfs(visited, i, j):
    union = [(i, j)]  # 연합에 속한 나라 좌표
    total_people = array[i][j]  # 연합의 인구수
    queue = deque([(i, j)])
    visited[i][j] = True

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 상하좌우 인접 나라 중 방문하지 않은 나라 방문 및 연합 처리
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if l <= abs(array[x][y] - array[nx][ny]) <= r:
                    total_people += array[nx][ny]
                    queue.append((nx, ny))
                    visited[nx][ny] = True
                    union.append((nx, ny))

    return union, total_people


result = 0
while move():
    result += 1
print(result)
