n, k = map(int, input().split())
arr = list(map(int, input().split()))  # 운동 키트 중량 증가량
used = [False] * n  # 운동 키트 사용 여부
result = 0


def dfs(day, weight):
    global result
    if day == n:  # n일간 중량 500 유지 가능
        result += 1
        return

    for i in range(n):
        # 사용하지 않았고 중량 500 이상 유지 가능할 경우에만 dfs
        if not used[i] and weight - k + arr[i] >= 500:
            used[i] = True
            dfs(day + 1, weight - k + arr[i])
            used[i] = False


dfs(0, 500)
print(result)
