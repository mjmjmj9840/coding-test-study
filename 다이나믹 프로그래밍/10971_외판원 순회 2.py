# 10971번: 외판원 순회 2

INF = int(1e9)
n = int(input())
w = [list(map(int, input().split())) for _ in range(n)]
# dp[visited][now]: visited 경로를 방문했고, now에서 0으로 돌아가기 위해 남은 비용ㄴ
dp = [[0] * n for _ in range(1 << n)]


def TSP(visited, now):
    if dp[visited][now] > 0:  # 이미 계산된 값이 있는 경우
        return dp[visited][now]

    # 모든 도시를 방문했을 경우
    if (visited + 1) == (1 << n):
        if w[now][0] > 0:  # 첫번째 도시로 돌아갈 수 있는 경우
            return w[now][0]
        else:  # 첫번째 도시로 돌아갈 수 없는 경우
            return INF

    dp[visited][now] = INF
    for i in range(n):
        # 방문하지 않았고 경로가 있는 도시일 경우
        if not (visited & (1 << i)) and w[now][i] > 0:
            dp[visited][now] = min(dp[visited][now], TSP(visited | (1 << i), i) + w[now][i])

    return dp[visited][now]


print(TSP(1, 0))
