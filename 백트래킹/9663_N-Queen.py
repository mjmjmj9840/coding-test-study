n = int(input())
visited1 = [False] * 30  # i번째 열에 퀸이 있는지
visited2 = [False] * 30  # i번째 ↗ 대각선에 퀸이 있는지
visited3 = [False] * 30  # i번째 ↘ 대각선에 퀸이 있는지
result = 0


def nQueen(x):
    global result
    if x == n:
        result += 1
        return

    for i in range(n):
        if visited1[i] or visited2[x + i] or visited3[x - i + n - 1]:
            continue
        visited1[i] = True
        visited2[x + i] = True
        visited3[x - i + n - 1] = True
        nQueen(x + 1)
        visited1[i] = False
        visited2[x + i] = False
        visited3[x - i + n - 1] = False


nQueen(0)
print(result)
