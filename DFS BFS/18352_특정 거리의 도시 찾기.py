# 18352번: 특정 거리의 도시 찾기

from collections import deque
import sys
input = sys.stdin.readline
INF = int(1e9)

# 도시 개수, 도로 개수, 최단 거리, 출발 도시
n, m, k, x = map(int, input().split())
# 각 도시에 연결된 도로 정보를 담는 리스트
graph = [[] for i in range(n + 1)]
# 최단 거리 테이블
distance = [INF] * (n + 1)

# 모든 도로 정보 입력 받기
for _ in range(m):
    i, j = map(int, input().split())
    graph[i].append(j)  # 도시 i에서 도시 j까지 도로가 존재

def solution(start):
    answer = []
    queue = deque([start])
    distance[start] = 0
    # bfs 방식으로 인접 도시들 방문
    while queue:
        v = queue.popleft()
        if distance[v] == k:
            answer.append(v)
        if distance[v] > k: # 나머지 도시들은 최단 거리가 k 이상
            return answer
        for x in graph[v]:
            # 현재 도시 v를 거쳐서 도시 x까지 가는게 더 짧은 경우
            if distance[v] + 1 < distance[x]:
                distance[x] = distance[v] + 1
                queue.append(x)
    
    return answer

answer = solution(x)
if answer:
    answer.sort()
    for x in answer: print(x)
else:
    print(-1)
