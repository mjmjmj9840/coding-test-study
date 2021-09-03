from collections import deque


def get_next_pos(pos, board):
    next_pos = []  # 이동할 수 있는 좌표 리스트
    pos = list(pos)
    x1, y1, x2, y2 = pos[0][0], pos[0][1], pos[1][0], pos[1][1]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(4):  # 상하좌우 이동
        nx1, ny1 = x1 + dx[i], y1 + dy[i]
        nx2, ny2 = x2 + dx[i], y2 + dy[i]
        if board[nx1][ny1] == 0 and board[nx2][ny2] == 0:
            next_pos.append({(nx1, ny1), (nx2, ny2)})
    if x1 == x2:  # 가로로 놓인 상태
        for i in [-1, 1]:
            # 위 또는 아래 두 칸이 비어있는 경우 회전 가능
            if board[x1 + i][y1] == 0 and board[x2 + i][y2] == 0:
                next_pos.append({(x1, y1), (x1 + i, y1)})
                next_pos.append({(x2, y2), (x2 + i, y2)})
    elif y1 == y2:  # 세로로 놓인 상태
        for i in [-1, 1]:
            # 왼쪽 또는 오른쪽 두 칸이 비어있는 경우 회전 가능
            if board[x1][y1 + i] == 0 and board[x2][y2 + i] == 0:
                next_pos.append({(x1, y1), (x1, y1 + i)})
                next_pos.append({(x2, y2), (x2, y2 + i)})

    return next_pos


def solution(board):
    cost = 0
    n = len(board)

    # 지도의 외곽을 1로 채우기
    new_board = [[1] * (n + 2) for _ in range(n + 2)]
    for i in range(n):
        for j in range(n):
            new_board[i + 1][j + 1] = board[i][j]

    # BFS
    pos = {(1, 1), (1, 2)}  # 시작 위치
    queue = deque([(pos, 0)])
    visited = [pos]

    while queue:
        pos, cost = queue.popleft()
        if (n, n) in pos:  # (n, n)에 도착할 경우
            return cost
        # 현재 위치에서 이동할 수 있는 위치
        for next_pos in get_next_pos(pos, new_board):
            if next_pos not in visited:
                queue.append((next_pos, cost + 1))
                visited.append(next_pos)

    return cost
