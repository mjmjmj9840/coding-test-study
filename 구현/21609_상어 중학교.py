# 21609번: 상어 중학교

import copy
from collections import deque

RAINBOW = 0
BLACK = -1
EMPTY = -2
VISITED = -3
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def autoplay(n):
    global array
    score = 0
    temp = copy.deepcopy(array)
    # 1. 크기가 가장 큰 블록 그룹 찾기
    block = findBiggestBlock(n, temp)
    if len(block) <= 1:  # 오토 플레이 중단
        return score

    # 2. 점수 획득 및 찾은 블록 그룹 제거
    score += len(block) ** 2
    for x, y in block:
        array[x][y] = EMPTY

    # 3. 중력 작용
    gravity(n, array)

    # 4. 90도 반시계 방향 회전
    array = rotate(n, array)

    # 5. 중력 작용
    gravity(n, array)

    return score


# 가장 큰 블록에 포함되는 좌표 리스트 반환
def findBiggestBlock(n, array):
    max_block = []
    max_rainbow = 0

    for i in range(n):
        for j in range(n):
            if array[i][j] <= RAINBOW:
                continue
            block, rainbow = bfs(array, i, j)
            if len(block) > len(max_block) or (len(block) >= len(max_block) and rainbow >= max_rainbow):
                max_block = block
                max_rainbow = rainbow

    return max_block


# (x, y)에서 시작되는 블록의 (블록 리스트, 무지개 블록 개수) 반환
def bfs(array, x, y):
    value = array[x][y]  # 일반블록 색상
    block = [(x, y)]  # 블록에 포함되는 좌표 리스트
    rainbow = 0  # 포함된 무지개 블록 개수
    queue = deque([(x, y)])
    array[x][y] = VISITED

    while queue:
        v = queue.popleft()
        for i in range(4):
            nx = v[0] + dx[i]
            ny = v[1] + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if array[nx][ny] == value:
                queue.append((nx, ny))
                array[nx][ny] = VISITED
                block.append((nx, ny))
            if array[nx][ny] == RAINBOW and (nx, ny) not in block:
                queue.append((nx, ny))
                rainbow += 1
                block.append((nx, ny))

    return block, rainbow


def gravity(n, array):
    for i in range(n - 1, -1, -1):
        for j in range(n):
            if array[i][j] <= BLACK:
                continue
            empty_row = i + 1  # 비어있는 가장 큰 행의 번호
            while empty_row < n:
                if array[empty_row][j] == EMPTY:
                    empty_row += 1
                else:
                    break
            # 블록 이동 시키기
            value = array[i][j]
            array[i][j] = EMPTY
            array[empty_row - 1][j] = value


def rotate(n, array):
    result = [[0] * n for _ in range(n)]

    for r in range(n):
        for c in range(n):
            result[n - c - 1][r] = array[r][c]

    return result


n, m = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(n)]
result = 0

while True:
    score = autoplay(n)
    if score == 0:
        break
    result += score

print(result)
