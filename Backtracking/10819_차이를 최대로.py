n = int(input())
arr = list(map(int, input().split()))
visited = [False] * n
result = 0


def dfs(depth, before, value):
    global result
    if depth == n - 1:
        result = max(result, value)

    for i in range(n):
        if not visited[i]:
            visited[i] = True
            dfs(depth + 1, arr[i], value + abs(before - arr[i]))
            visited[i] = False


for i in range(n):
    visited[i] = True
    dfs(0, arr[i], 0)
    visited[i] = False

print(result)
