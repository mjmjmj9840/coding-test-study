''' BFS '''

from collections import deque

def bfs(graph, start, visited):
  queue = deque([start])
  visited[start] = True

  while queue:
    v = queue.popleft()
    for i in graph[v]:
      if not visited[i]:
        queue.append(i)
        visited[i] = True

        
        
        
''' 사용 예시 '''

# 노드의 개수, 간선의 개수, 탐색 시작 지점
v, e, start = map(int, input().split())

graph = [[] for _ in range(v + 1)]
visited = [False] * (v + 1)

# 간선 정보 입력 받기(양방향 그래프 가정)
for _ in range(e):
  a, b = map(int, input())
  graph[a].append(b)
  graph[b].append(a)
  
bfs(graph, start, visited)


# 시간 복잡도: O(V + E)
