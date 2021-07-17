'''
    크루스칼 알고리즘
    : 최소 신장 트리(Minimum Spanning Tree)를 찾는 알고리즘

    신장 트리(Spanning Tree)
    : 하나의 그래프가 있을 때 모든 노드를 포함하면서 사이클이 존재하지 않은 부분 그래프
'''

# 특정 원소가 속한 집합 찾기
def find_parent(parent, x):
    # 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


# 두 원소가 속한 집합 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


# 노드와 간선(Union 연산)의 개수 입력
v, e = map(int, input().split())
parent = [0] * (v + 1) # 부모 테이블 초기화

# 간선 리스트와, 최종 비용을 담을 변수
edges = []
result = 0

# 부모를 자기 자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i

# 간선 정보 입력
for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

# 간선을 비용순으로 정렬
edges.sort()

# 모든 간선 확인
for edge in edges:
    cost, a, b = edge
    # 사이클이 발생하지 않는 경우에만 집합에 포함
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(result)


# 시간 복잡도: O(ElogE)
