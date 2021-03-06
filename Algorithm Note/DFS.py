''' DFS '''

def dfs(graph, v, visited):
  visited[v] = True
  
  for i in graph[v]:
    if not visited[i]:
      dfs(graph, i, visited)




# 사용 예시
graph = [
  [],
  [2, 3, 8],
  [1, 7],
  [1, 4, 5],
  [3, 5],
  [3, 4],
  [7],
  [2, 6, 8],
  [1, 7]
]
visited = [False] * 9
dfs(graph, 1, visited)


# 시간 복잡도: O(V + E)
