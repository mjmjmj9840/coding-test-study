# 2346번: 풍선 터뜨리기

n = int(input())
array = list(map(int, input().split()))
array *= 2  # 원형을 일자형태로 바꾸기

move = array[0]
array[0] = 0  # 터진 풍선을 0으로 표현
array[n] = 0
print(1, end=' ')  # 1번 풍선부터 터뜨림
pos = 0 if move > 0 else n  # 현재 위치

for _ in range(n - 1):
    while move > 0:
        pos = (pos + 1) % n
        if array[pos] != 0:
            move -= 1
    while move < 0:
        pos = (pos - 1) % n
        if array[pos] != 0:
            move += 1

    print(pos + 1, end=' ')
    move = array[pos]
    array[pos] = 0
    array[pos + n] = 0
    pos = pos if move > 0 else pos + n
