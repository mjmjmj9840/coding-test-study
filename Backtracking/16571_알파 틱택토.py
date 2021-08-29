board = []  # 게임 보드
empty = []  # 게임 보드 빈칸 좌표
start = 0  # 이번에 착수하는 플레이어


def win(player):
    for x in range(3):  # 가로 한 줄
        if board[x][0] == player and board[x][0] == board[x][1] and board[x][1] == board[x][2]:
            return True

    for y in range(3):  # 세로 한 줄
        if board[0][y] == player and board[0][y] == board[1][y] and board[1][y] == board[2][y]:
            return True

    # 대각선 한 줄
    if board[0][0] == player and board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        return True

    if board[0][2] == player and board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        return True

    return False

# WIN: 1, DRAW: 0, LOSE: -1
def play(player, empty):
    # 상대가 이겼다면 LOSE 반환
    if win(3 - player):
        return -1

    result = 2
    for i in range(len(empty)):
        x = empty[i][0]
        y = empty[i][1]
        board[x][y] = player
        result = min(result, play(3 - player, empty[:i] + empty[i + 1:]))
        board[x][y] = 0

    if result == 2:  # 빈 공간이 없는 경우
        return 0
    return -result  # 상대가 WIN이면 나는 LOSE


for i in range(3):
    board.append(list(map(int, input().split())))
    for j in range(3):
        if board[i][j] == 0:
            empty.append((i, j))

start = 1 if len(empty) % 2 == 1 else 2
result = play(start, empty)

if result == 1:
    print('W')
elif result == 0:
    print('D')
else:
    print('L')