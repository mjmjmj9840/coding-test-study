# NxM 2차원 리스트 90도 회전
def rotate_a_matrix_by_90_degree(array):
    n = len(array)  # 행 길이
    m = len(array[0])  # 열 길이

    result = [[0] * n for _ in range(m)]
    for r in range(n):
        for c in range(m):
            result[c][n - 1 - r] = array[r][c]

    return result


# NxN 2차원 리스트 d도 회전
# 회전 각도 d => 1: 90도, 2: 180도, 3: 270도
def rotate(array, d):
    n = len(array)  # 배열의 길이
    result = [[0] * n for _ in range(n)]

    if d % 4 == 1:
        for r in range(n):
            for c in range(n):
                result[c][n - r - 1] = array[r][c]
    elif d % 4 == 2:
        for r in range(n):
            for c in range(n):
                result[n - r - 1][n - c - 1] = array[r][c]
    elif d % 4 == 3:
        for r in range(n):
            for c in range(n):
                result[n - c - 1][r] = array[r][c]
    else:
        for r in range(n):
            for c in range(n):
                result[r][c] = array[r][c]

    return result
