'''
    위상 정렬(Topology Sort)
    : 방향 그래프의 모든 노드를 방향성에 거스르지 않도록 순서대로 나열하는 것
'''


from collections import deque

# 노드와 간선의 개수 입력
v, e = map(int, input().split())
# 모든 노드의 진입차수 0으로 초기화
indegree = [0] * (v + 1)
# 그래프 리스트 초기화
graph = [[] for i in range(v + 1)]

# 간선 정보 입력(방향 그래프)
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)  # 노드 A에서 B로 이동 가능
    # 진입 차수 1 증가
    indegree[b] += 1


# 위상 정렬 함수
def topology_sort():
    result = []  # 알고리즘 수행 결과 노드 순서 리스트
    q = deque()

    # 진입차수가 0인 노드 큐에 삽입
    for i in range(1, v + 1):
        if indegree[i] == 0:
            q.append(i)

    # 큐가 빌 때까지 반복
    while q:
        # 큐에서 원소 꺼내기
        now = q.popleft()
        result.append(now)
        # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
        for i in graph[now]:
            indegree[i] -= 1
            # 새롭게 진입차수가 0이 되는 노드 큐에 삽입
            if indegree[i] == 0:
                q.append(i)

    # 위상 정렬 수행 결과 출력
    for i in result:
        print(i, end=' ')


topology_sort()


# 시간 복잡도: O(V + E)
