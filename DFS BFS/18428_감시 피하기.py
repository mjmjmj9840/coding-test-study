# 18428번: 감시 피하기

from itertools import combinations


# (x, y)에 있는 학생이 감시를 피할 수 있는지 판단
def safe(n, array, x, y):
    i, j = x, y
    while i > 0:
        i -= 1
        if array[i][j] == 'O':
            break
        elif array[i][j] == 'T':
            return False

    i, j = x, y
    while i < n - 1:
        i += 1
        if array[i][j] == 'O':
            break
        elif array[i][j] == 'T':
            return False

    i, j = x, y
    while j > 0:
        j -= 1
        if array[i][j] == 'O':
            break
        elif array[i][j] == 'T':
            return False

    i, j = x, y
    while j < n - 1:
        j += 1
        if array[i][j] == 'O':
            break
        elif array[i][j] == 'T':
            return False

    return True


n = int(input())
array = []  # 전체 복도 정보
empty = []  # 비어있는 좌표(장애물을 설치할 수 있는 곳)
for i in range(n):
    data = list(input().split())
    array.append(data)
    for j in range(n):
        if data[j] == 'X':
            empty.append((i, j))

# 완전 탐색
for a, b, c in combinations(empty, 3):
    # a, b, c 3군데에 장애물 설치
    array[a[0]][a[1]] = 'O'
    array[b[0]][b[1]] = 'O'
    array[c[0]][c[1]] = 'O'
    all_safe = True  # 모든 학생이 감시를 피할 수 있는지
    for i in range(n):
        for j in range(n):
            if array[i][j] == 'S':
                # 감시를 피할 수 있는지 확인
                if not safe(n, array, i, j):
                    all_safe = False
                    break
        if not all_safe:
            break
    if all_safe:
        break

    # a, b, c 3군데에 장애물 없애기
    array[a[0]][a[1]] = 'X'
    array[b[0]][b[1]] = 'X'
    array[c[0]][c[1]] = 'X'

if all_safe:
    print("YES")
else:
    print("NO")
