# union-find

# 특정 원소가 속한 집합 찾기
def find_parent(parent, i):
    if parent[i] != i:
        parent[i] = find_parent(parent, parent[i])

    return parent[i]


# 두 원소의 집합 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


N, M = map(int, input().split())
parent = [0] * (N + 1)
for i in range(N + 1):
    parent[i] = i

for _ in range(M):
    op, a, b = map(int, input().split())
    # 팀 합치기
    if op == 0:
        union_parent(parent, a, b)
    # 같은 팀 여부 확인
    else:
        if find_parent(parent, a) == find_parent(parent, b):
            print("YES")
        else:
            print("NO")
