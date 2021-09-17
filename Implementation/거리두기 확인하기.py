# (x, y)의 사람이 거리 두기를 지키고 있는지 확인
def check(place, x, y):
    dx = [-1, 1, 0, 0]  # 상 하 좌 우
    dy = [0, 0, -1, 1]
    is_okay = True

    for i in range(4):
        nx1, ny1 = x + dx[i], y + dy[i]
        if nx1 < 0 or nx1 >= 5 or ny1 < 0 or ny1 >= 5:
            continue
        if place[nx1][ny1] == 'X':  # 가림막이 있을 경우
            continue
        if place[nx1][ny1] == 'P':  # 거리두기 안지킨 경우
            is_okay = False
            break
        for j in range(4):  # 다음 칸으로 이동(맨해튼 거리 2)
            nx2, ny2 = nx1 + dx[j], ny1 + dy[j]
            if nx2 < 0 or nx2 >= 5 or ny2 < 0 or ny2 >= 5:
                continue
            if place[nx2][ny2] == 'X':  # 가림막이 있을 경우
                continue
            if place[nx2][ny2] == 'P' and not (nx2 == x and ny2 == y):  # 거리두기 안지킨 경우
                is_okay = False
                break

    return is_okay


def solution(places):
    answer = []

    for place in places:
        observe = True
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P' and not check(place, i, j):
                    observe = False
                    break
            if not observe:
                break

        answer.append(1) if observe else answer.append(0)

    return answer
