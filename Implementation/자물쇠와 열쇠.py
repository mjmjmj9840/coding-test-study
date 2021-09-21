# key를 시계 방향 90도 회전
def rotate(key, m):
    result = [[0] * m for _ in range(m)]
    for i in range(m):
        for j in range(m):
            result[i][j] = key[j][m - i - 1]

    return result


# key를 더하거나 빼기
def useKey(i, j, key, my_lock, op):
    for x in range(len(key)):
        for y in range(len(key)):
            my_lock[i + x][j + y] += key[x][y] * op


# 자물쇠가 모두 열렸는지 확인
def isOpen(my_lock, n):
    for i in range(n):
        for j in range(n):
            if my_lock[n + i][n + j] != 1:
                return False
    return True


def solution(key, lock):
    n, m = len(lock), len(key)
    my_lock = [[0] * 3 * n for _ in range(3 * n)]  # 기존 자물쇠의 3배 크기 좌물쇠 만들기
    # 새로운 자물쇠 중앙에 lock 복사
    for i in range(n):
        for j in range(n):
            my_lock[i + n][j + n] = lock[i][j]

    for r in range(4):  # 네방향 회전
        for i in range(1, 2 * n):
            for j in range(1, 2 * n):
                useKey(i, j, key, my_lock, 1)  # key 더하기
                if isOpen(my_lock, n):
                    return True
                useKey(i, j, key, my_lock, -1)  # key 빼기
        key = rotate(key, m)

    return False
