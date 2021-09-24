from collections import deque


def get_next_pos(board, pos1, pos2):
    next_pos = []  # 이동 가능한 위치 정보

    # 상 하 좌 우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    # 이동
    for i in range(4):
        nx1, ny1 = pos1[0] + dx[i], pos1[1] + dy[i]
        nx2, ny2 = pos2[0] + dx[i], pos2[1] + dy[i]
        # 이동할 수 있는 경우
        if board[nx1][ny1] == 0 and board[nx2][ny2] == 0:
            next_pos.append(((nx1, ny1), (nx2, ny2)))

    # 회전
    # 로봇이 가로로 놓인 경우
    if pos1[0] == pos2[0]:
        # 위쪽 두 칸이 비어있으면 회전 가능
        if board[pos1[0] - 1][pos1[1]] == 0 and board[pos2[0] - 1][pos2[1]] == 0:
            next_pos.append(((pos1[0], pos1[1]), (pos1[0] - 1, pos1[1])))
            next_pos.append(((pos2[0], pos2[1]), (pos2[0] - 1, pos2[1])))
        # 아래쪽 두 칸이 비어있으면 회전 가능
        if board[pos1[0] + 1][pos1[1]] == 0 and board[pos2[0] + 1][pos2[1]] == 0:
            next_pos.append(((pos1[0], pos1[1]), (pos1[0] + 1, pos1[1])))
            next_pos.append(((pos2[0], pos2[1]), (pos2[0] + 1, pos2[1])))
    # 로봇이 세로로 놓인 경우
    else:
        # 왼쪽 두 칸이 비어있으면 회전 가능
        if board[pos1[0]][pos1[1] - 1] == 0 and board[pos2[0]][pos2[1] - 1] == 0:
            next_pos.append(((pos1[0], pos1[1]), (pos1[0], pos1[1] - 1)))
            next_pos.append(((pos2[0], pos2[1]), (pos2[0], pos2[1] - 1)))
        # 오른쪽 두 칸이 비어있으면 회전 가능
        if board[pos1[0]][pos1[1] + 1] == 0 and board[pos2[0]][pos2[1] + 1] == 0:
            next_pos.append(((pos1[0], pos1[1]), (pos1[0], pos1[1] + 1)))
            next_pos.append(((pos2[0], pos2[1]), (pos2[0], pos2[1] + 1)))

    return next_pos


# (1, 1)에서 (n, n)에 도착할 때까지 BFS
def bfs(board, n):
    # ({좌표1, 좌표2}, cost)로 로봇의 이동 표현
    queue = deque([(((1, 1), (1, 2)), 0)])
    visited = [{(1, 1), (1, 2)}]

    while queue:
        (pos1, pos2), cost = queue.popleft()
        if (n, n) in [pos1, pos2]:  # 목적지 도착
            return cost

        for npos1, npos2 in get_next_pos(board, pos1, pos2):
            # 방문하지 않은 경우
            if {(npos1, npos2)} not in visited:
                queue.append(((npos1, npos2), cost + 1))
                visited.append({(npos1, npos2)})


def solution(board):
    n = len(board)
    # board 외곽을 1로 채우기
    my_board = [[1] * (n + 2) for _ in range(n + 2)]
    for i in range(n):
        for j in range(n):
            my_board[i + 1][j + 1] = board[i][j]

    answer = bfs(my_board, n)

    return answer
