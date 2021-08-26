n, m = map(int, input().split())
arr = [0] * m


def dfs(depth):
    if depth == m:  # m가지 숫자를 모두 뽑은 경우
        print(' '.join(map(str, arr)))
        return

    for i in range(1, n + 1):
        arr[depth] = i
        dfs(depth + 1)


dfs(0)
