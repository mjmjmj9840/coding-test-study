import sys

sys.setrecursionlimit(10 ** 6)

answer = []
visited = []  # visited[x][y][d]: (x, y) 위치의 칸을 d 방향으로 방문
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 다음으로 이동할 빛의 방향 구하기
def getDirection(s, d):
    if s == 'S':  # 직진
        return d
    elif s == 'L':  # 좌회전
        nd = [2, 3, 1, 0]  # 좌우하상
        return nd[d]
    else:  # 우회전
        nd = [3, 2, 0, 1]
        return nd[d]

    
def dfs(grid, start, now, depth):
    global visited, answer
    visited[now[0]][now[1]][now[2]] = True
    
    # 빛이 이동하는 방향과 다음 칸
    nd = getDirection(grid[now[0]][now[1]], now[2])
    nx = now[0] + dx[nd]
    ny = now[1] + dy[nd]
    # 빛이 격자 끝을 넘어가는 경우 처리
    if nx < 0:
        nx = len(grid) - 1
    elif nx >= len(grid):
        nx = 0  
    if ny < 0:
        ny = len(grid[0]) - 1
    elif ny >= len(grid[0]):
        ny = 0

    # 사이클이 존재하는 경우
    if (nx, ny, nd) == start:
        answer.append(depth)
        return
    
    # 해당 칸을 해당 빛의 방향으로 방문하지 않은 경우
    if not visited[nx][ny][nd]:
        dfs(grid, start, (nx, ny, nd), depth + 1)


def solution(grid):
    global visited, answer
    visited = [[[False] * 4 for _ in range(len(grid[0]))] for _ in range(len(grid))]
    # 모든 칸에 상하좌우로 빛을 쏘았을 때 사이클 판별
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            for d in range(4):
                dfs(grid, (i, j, d), (i, j, d), 1)
    
    return sorted(answer)