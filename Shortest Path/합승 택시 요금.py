def solution(n, s, a, b, fares):
    INF = int(1e9)
    answer = INF
    graph = [[INF] * (n + 1) for _ in range(n + 1)]

    # 자기 자신으로 가는 비용 초기화
    for i in range(1, n + 1):
        graph[i][i] = 0

    # 간선 정보 입력
    for i, j, c in fares:
        graph[i][j] = c
        graph[j][i] = c

    # 플로이드 워셜 알고리즘
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

    # k 지점까지 합승할 경우 최소 비용
    for k in range(1, n + 1):
        answer = min(answer, graph[s][k] + graph[k][a] + graph[k][b])

    return answer
