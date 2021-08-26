# 2606번: 바이러스

import sys
from collections import deque

input = sys.stdin.readline


def bfs(graph, start, visited):
    global result
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                result += 1


v = int(input())
e = int(input())
graph = [[] for _ in range(v + 1)]
visited = [False] * (v + 1)
result = 0
# 네트워크 정보 입력 받기
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

bfs(graph, 1, visited)
print(result)
