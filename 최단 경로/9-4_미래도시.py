INF = int(1e9)

N, M = map(int, input().split())
graph = [[INF] * (N + 1) for _ in range(N + 1)]
# 자기자신으로 가는 비용 0으로 초기화
for i in range(N + 1):
    graph[i][i] = 0
# 인접 노드 정보 입력받기
for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1
X, K = map(int, input().split())

# 플로이드 워셜 알고리즘
for i in range(1, N + 1):
    for j in range(1, N + 1):
        for k in range(1, N + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

distance = graph[1][K] + graph[K][X]
if distance >= INF:
    print(-1)
else:
    print(distance)
