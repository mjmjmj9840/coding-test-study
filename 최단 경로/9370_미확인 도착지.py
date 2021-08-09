# 9370번: 미확인 도착지

import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)
T = int(input())


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    while q:
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[now] < dist:
            continue
        # 현재 노드와 인접한 노드들 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서 인접 노드로 가는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


for _ in range(T):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    distance = [INF] * (n + 1)  # 최단 거리 테이블

    # 간선 비용 입력 받기
    for _ in range(m):
        a, b, d = map(int, input().split())
        # g, h 노드 사이의 간선 비용은 홀수로 저장
        if (a == g and b == h) or (a == h and b == g):
            graph[a].append((b, d * 2 - 1))
            graph[b].append((a, d * 2 - 1))
        # 나머지 간선 비용은 짝수로 저장
        else:
            graph[a].append((b, d * 2))
            graph[b].append((a, d * 2))

    # 목적지 후보 입력 받기
    destination = [int(input()) for _ in range(t)]
    destination.sort()
    # s를 출발점으로 모든 노드에 대한 최단 거리 구하기
    dijkstra(s)

    for x in destination:
        # 최단 거리가 홀수일 경우 g, h를 지남
        if distance[x] % 2 == 1:
            print(x, end=' ')
