/*
크루스칼 알고리즘
: 최소 신장 트리(Minimum Spanning Tree)를 찾는 알고리즘

신장 트리(Spanning Tree)
: 하나의 그래프가 있을 때 모든 노드를 포함하면서 사이클이 존재하지 않은 부분 그래프
*/

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

// 노드 개수, 간선(Union 연산) 개수
// 노드의 개수는 최대 100,000개라고 가정
int v, e;
int parent[100001]; // 부모 테이블
vector<pair<int, pair<int, int> > > edges;
int result = 0;  // 최종 비용

int findParent(int x) {
    if (x == parent[x]) return x;
    return parent[x] = findParent(parent[x]);
}

void unionParent(int a, int b) {
    a = findParent(a);
    b = findParent(b);
    if (a < b) parent[b] = a;
    else parent[a] = b;
}

int main() {
    cin >> v >> e;

    // 부모 테이블 초기화
    for (int i = 1; i <= v; i++)
        parent[i] = i;

    // 간선 입력
    for (int i = 0; i < e; i++) {
        int a, b, cost;
        cin >> a >> b >> cost;
        // 비용 오름차순
        edges.push_back({cost, {a, b}});
    }

    // 간선을 비용순으로 정렬
    sort(edges.begin(), edges.end());

    // 모든 간선 확인
    for (int i = 0; i < edges.size(); i++) {
        int cost = edges[i].first;
        int a = edges[i].second.first;
        int b = edges[i].second.second;
        // 사이클이 발생하지 않는 경우에만 집합에 포함
        if (findParent(a) != findParent(b)) {
            unionParent(a, b);
            result += cost;
        }
    }

    cout << result << '\n';
}

// 시간 복잡도: O(ElogE)

/*
input example
7 9
1 2 29
1 5 75
2 3 35
2 6 34
3 4 7
4 6 23
4 7 13
5 6 53
6 7 25

output
159
*/