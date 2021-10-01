# 지울 수 있는 5개의 블록의 모양
blocks = [
    [(1, 0), (1, 1), (1, 2)], 
    [(1, 0), (2, -1), (2, 0)], 
    [(1, 0), (2, 0), (2, 1)], 
    [(1, -2), (1, -1), (1, 0)], 
    [(1, -1), (1, 0), (1, 1)]
]

# 지울 수 있는 5개 블록 모양 별로 채워야하는 칸
fill = [
    [(0, 1), (0, 2)], 
    [(0, -1), (1, -1)],
    [(0, 1), (1, 1)], 
    [(0, -2), (0, -1)], 
    [(0, -1), (0, 1)]
]

def solution(board):
    answer = 0
    n = len(board)  # 보드 크기
    checked = [0] * 201  # 확인한 블록 숫자
    checked[0] = 1
    deletable = []  # 지울 수 있는 모양 블록 (시작 인덱스, 블록 모양 번호)
    
    # 지울 수 있는 모양인 블록 찾기
    for i in range(n):
        for j in range(n):
            # 이미 체크한 블록일 경우
            if checked[board[i][j]]:
                continue
            # 5가지 블록 모양 중 맞는 모양 매칭
            for b_idx in range(5):
                match = True
                for k in range(3):
                    x, y = blocks[b_idx][k]
                    if i + x < 0 or i + x >= n or j + y < 0 or j + y >= n:
                        match = False
                        break
                    if board[i][j] != board[i + x][j + y]:
                        match = False
                        break
                # 맞는 모양 블록을 찾은 경우
                if match:
                    deletable.append(((i, j), b_idx))
                    checked[board[i][j]] = 1
                    break
    
    # 블록을 하나씩 삭제
    while deletable:
        delete = False
        for idx in range(len(deletable)):
            possible = True
            (i, j), b_idx = deletable[idx]
            # 검은 블록을 떨어뜨릴 위치 위에 다른 블록이 있으면 안됨
            for x, y in fill[b_idx]:
                for row in range(i + x + 1):
                    if board[row][j + y] != 0:
                        possible = False
                        break
            # 블록 삭제
            if possible:
                board[i][j] = 0
                for x, y in blocks[b_idx]:
                    board[i + x][j + y] = 0
                deletable.pop(idx)
                answer += 1
                delete = True
                break
        # 지울 블록이 없는 경우
        if not delete:
            break
    
    return answer