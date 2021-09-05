# 테스트케이스 7, 10, 17, 19, 25, 28 틀리는데 진짜 모르겠음,,

from itertools import permutations
from collections import deque
from collections import defaultdict

answer = 987654321


# (x, y)에서 다음에 갈 수 있는 모든 좌표 구하기
def get_next_pos(x, y, board):
    next_pos = set()  # 이동 가능한 좌표
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(4):  # 상하좌우 이동
        nx, ny = x, y
        while 0 <= nx + dx[i] < 4 and 0 <= ny + dy[i] < 4:
            nx, ny = nx + dx[i], ny + dy[i]
            next_pos.add((nx, ny))
            if board[nx][ny] != 0:  # 제일 가까운 카드에서 멈춤
                break

    return next_pos


# start에서 end로 가능 최소 비용 반환
def find_card(start, end, board):
    q = deque([(start, 0)])
    visited = [start]

    while q:  # BFS
        v, cost = q.popleft()
        if end == v:  # end에 도착한 경우
            return cost
        for next_pos in get_next_pos(v[0], v[1], board):
            if next_pos not in visited:
                q.append((next_pos, cost + 1))
                visited.append(next_pos)

    return 0


def backtracking(cand, card, cursor, cost, board):
    global answer
    if not cand:  # 모든 카드를 제거한 경우
        answer = min(answer, cost)
        return

    n = cand[0]  # 제거할 카드 번호
    pos = list(permutations(card[n]))  # (시작, 끝) 경우의 수

    for start, end in pos:
        temp = find_card(cursor, start, board) + 1  # 시작 카드로 이동 + enter
        temp += find_card(start, end, board) + 1  # 끝 카드로 이동 + enter
        board[start[0]][start[1]] = 0  # 카드 삭제
        board[end[0]][end[1]] = 0
        backtracking(cand[1:], card, end, cost + temp, board)
        board[start[0]][start[1]] = n  # 카드 복구
        board[end[0]][end[1]] = n


def solution(board, r, c):
    global answer
    card = defaultdict(list)  # 카드 번호: 카드 좌표 리스트
    for i in range(4):
        for j in range(4):
            if board[i][j] != 0:
                card[board[i][j]].append((i, j))

    candidates = list(permutations([key for key in card.keys()]))  # 카드 제거 순서 경우의 수
    for cand in candidates:
        backtracking(cand, card, (r, c), 0, board)

    return answer
