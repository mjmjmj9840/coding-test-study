# 1717번: 집합의 표현
import sys

sys.setrecursionlimit(1000001)
input = sys.stdin.readline

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


n, m = map(int, input().split())
parent = [0] * (n + 1)  # 부모 테이블 초기화

# 부모를 자기 자신으로 초기화
for i in range(1, n + 1):
    parent[i] = i

# 각 연산 입력 받기
for _ in range(m):
    op, a, b = map(int, input().split())
    # 합집합 연산
    if op == 0:
        union_parent(parent, a, b)
    # 같은 집합에 포함되어 있는지 확인하는 연산
    else:
        if find_parent(parent, a) == find_parent(parent, b):
            print("YES")
        else:
            print("NO")
