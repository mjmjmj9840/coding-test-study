dx = [0, 1, 0, -1]  # 우 하 좌 상(시계방향)
dy = [1, 0, -1, 0]


def rotate(r1, c1, r2, c2, array):
    x, y = r1, c1  # 이번에 회전할 칸의 위치
    value = array[x][y]  # 이번에 회전할 칸의 값
    min_value = value  # 회전한 값들 중 최솟값
    d = 0  # 이동할 방향

    while True:  # 시계방향 회전
        nx, ny = x + dx[d], y + dy[d]
        if nx < r1 or nx > r2 or ny < c1 or ny > c2:
            d += 1  # 방향 전환
            continue

        array[nx][ny], value = value, array[nx][ny]
        min_value = min(min_value, value)
        x, y = nx, ny

        if x == r1 and y == c1:  # 처음 위치로 돌아온 경우
            break

    return min_value


def solution(rows, columns, queries):
    answer = []
    array = [[i * (columns) + j + 1 for j in range(columns)] for i in range(rows)]  # 회전할 행렬 만들기

    for r1, c1, r2, c2 in queries:
        answer.append(rotate(r1 - 1, c1 - 1, r2 - 1, c2 - 1, array))

    return answer
