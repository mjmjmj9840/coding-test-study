# 15649번: N과 M (1)

n, m = map(int, input().split())
arr = [0] * m
visited = [False] * (n + 1)

def dfs(depth):
    if depth == m:  # m가지 숫자를 모두 뽑은 경우
        print(' '.join(map(str, arr)))
        return

    for i in range(1, n + 1):
        if not visited[i]:
            visited[i] = True
            arr[depth] = i
            dfs(depth + 1)
            visited[i] = False

dfs(0)
