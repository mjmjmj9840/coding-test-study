# 위상 정렬
import copy
from collections import deque

N = int(input())
# 모든 노드의 진입차수 0으로 초기화
indegree = [0] * (N + 1)
# 그래프 리스트 초기화
graph = [[] for i in range(N + 1)]
# 강의 시간 리스트
time = [0] * (N + 1)

# 강의 정보 입력
for i in range(1, N + 1):
    data = list(map(int, input().split()))
    time[i] = data[0]
    for pre in data[1:-1]:
        graph[pre].append(i)  # 노드 pre에서 i로 가는 간선
        indegree[i] += 1  # 진입 차수 1 증가


# 위상 정렬 함수
def topology_sort():
    result = copy.deepcopy(time)  # 강의 수강까지 걸리는 최소 시간
    q = deque()

    # 진입차수가 0인 노드 큐에 삽입
    for i in range(1, N + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        # 큐에서 원소 꺼내기
        now = q.popleft()
        for i in graph[now]:
            # 선수 강의 수강 시간이 더 오래걸릴 경우 갱신
            result[i] = max(result[i], result[now] + time[i])
            indegree[i] -= 1
            # 새롭게 진입차수가 0이 되는 노드 큐에 삽입
            if indegree[i] == 0:
                q.append(i)

    for i in range(1, N + 1):
        print(result[i])


topology_sort()
