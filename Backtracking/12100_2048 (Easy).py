import sys, copy

input = sys.stdin.readline
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
result = 0


# up: 0, down: 1, left:2, right: 3
def move(arrow):
    if arrow % 2 == 0:  # up, left
        start, end, step = 1, n, 1
    else:  # down, right
        start, end, step = n - 2, -1, -1

    if arrow < 2:  # up, down
        for j in range(n):
            k = start - step  # 제일 끝쪽에서 시작
            for i in range(start, end, step):
                if board[i][j] == 0:  # 빈 칸일 경우 무시
                    continue
                temp, board[i][j] = board[i][j], 0
                if board[k][j] == 0:  # 빈 칸일 경우 이동
                    board[k][j] = temp
                elif board[k][j] == temp:  # 같은 수일 경우 합침
                    board[k][j] = temp * 2
                    k += step
                else:  # 그대로 둠
                    k += step
                    board[k][j] = temp

    else:  # left, right
        for i in range(n):
            k = start - step  # 제일 끝쪽에서 시작
            for j in range(start, end, step):
                if board[i][j] == 0:  # 빈 칸일 경우 무시
                    continue
                temp, board[i][j] = board[i][j], 0
                if board[i][k] == 0:  # 빈 칸일 경우 이동
                    board[i][k] = temp
                elif board[i][k] == temp:  # 같은 수일 경우 합침
                    board[i][k] = temp * 2
                    k += step
                else:  # 그대로 둠
                    k += step
                    board[i][k] = temp


def play(cnt):
    global result, board

    if cnt == 5:
        for i in range(n):
            for j in range(n):
                result = max(result, board[i][j])
        return

    original = copy.deepcopy(board)  # 원본 배열 저장

    for i in range(4):
        move(i)
        play(cnt + 1)
        board = copy.deepcopy(original)  # 보드 원상복구


play(0)
print(result)
