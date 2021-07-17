# 크루스칼 알고리즘

import sys

input = sys.stdin.readline


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])

    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


N, M = map(int, input().split())

edges = []
result = 0
parent = [0] * (N + 1)

for i in range(N + 1):
    parent[i] = i

for _ in range(M):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort()
last = 0  # MST의 간선 중에서 가장 큰 비용

for edge in edges:
    cost, a, b = edge
    # 사이클 발생하지 않으면 집합에 포함
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
        last = cost

# 2개 MST의 비용을 찾기 위해 마지막 간선 제외하고 답 반환
print(result - last)
