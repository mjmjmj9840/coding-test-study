/*
위상 정렬(Topology Sort)
: 방향 그래프의 모든 노드를 방향성에 거스르지 않도록 순서대로 나열하는 것
*/

#include <iostream>
#include <vector>
#include <queue>
using namespace std;

// 노드 개수와 간선 개수
// 노드의 개수는 최대 100,000개라고 가정
int v, e;
int indegree[100001];  // 진입차수
// 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트 초기화
vector<int> graph[100001];

void topologySort() {
    vector<int> result;
    queue<int> q;

    // 진입차수가 0인 노드를 큐에 삽입하고 시작
    for (int i = 1; i <= v; i++)
        if (indegree[i] == 0)
            q.push(i);

    while (!q.empty()) {
        int now = q.front();
        q.pop();
        result.push_back(now);
        // 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
        for (int i = 0; i < graph[now].size(); i++) {
            indegree[graph[now][i]] -= 1;
            // 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
            if (indegree[graph[now][i]] == 0)
                q.push(graph[now][i]);
        }
    }

    // 위상 정렬 수행 결과 출력
    for (int i = 0; i < result.size(); i++)
        cout << result[i] << ' ';
}

int main() {
    cin >> v >> e;

    // 방향 그래프의 간선 정보 입력
    for (int i = 0; i < e; i++) {
        int a, b;
        cin >> a >> b;
        graph[a].push_back(b); // 정점 A에서 B로 이동 가능
        // 진입 차수 갱신
        indegree[b] += 1;
    }

    topologySort();
}

// 시간 복잡도: O(V + E)

/*
input example
7 8
1 2
1 5
2 3
2 6
3 4
4 7
5 6
6 4

output
1 2 5 3 6 4 7
*/