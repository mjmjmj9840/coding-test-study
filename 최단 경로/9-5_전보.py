import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

N, M, C = map(int, input().split())
graph = [[] for _ in range(N + 1)]
distance = [INF] * (N + 1)
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


# 다익스트라 알고리즘으로 각 노드까지의 최단 거리 구하기
def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        # 이미 처리한적 있는 노드
        if distance[now] < dist:
            continue
        # 인접 노드의 거리 정보 갱신
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(C)
num_cities = 0
total_time = 0
for i in range(1, N + 1):
    if distance[i] != INF:
        num_cities += 1
        total_time = max(total_time, distance[i])
# 자기 자신은 갈 수 있는 도시의 개수에서 뺀다
print(num_cities - 1, total_time)
