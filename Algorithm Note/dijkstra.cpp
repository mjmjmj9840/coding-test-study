/*
출발 노드에서 다른 노드로 가는 각각의 최단 경로 구하기
*/
#include <iostream>
#include <queue>
#include <vector>
#include <algorithm>
#define INF 1e9
using namespace std;

// 노드 개수, 간선 개수, 시작 노드 번호
int n, m, start;
// 각 노드에 연결된 노드 정보
// 최대 노드 개수 100000개 가정
vector<pair<int, int>> graph[100001];
// 최단 거리 테이블
int d[100001];

void dijkstra(int start) {
	priority_queue<pair<int, int>> pq;
	// 시작 노드 큐에 삽입
	pq.push({0, start});
	d[start] = 0;
	while (!pq.empty()) {
		// 최단 거리가 가장 짧은 노드 꺼내기
		int dist = -pq.top().first;  // 현재 노드까지의 비용
		int now = pq.top().second;  // 현재 노드
		pq.pop();
		// 현재 노드가 이미 처리되었다면 무시
		if (d[now] < dist) continue;
		// 현재 노드와 인접한 노드 확인
		for (int i = 0; i < graph[now].size(); i++) {
			int cost = dist + graph[now][i].second;
			// 현재 노드를 거치는게 더 짧은 경우
			if (cost < d[graph[now][i].first]) {
				d[graph[now][i].first] = cost;
				// 내림차순 우선순위 큐
				pq.push(make_pair(-cost, graph[now][i].first));
			}
		}
	}
}

int main() {
    cin >> n >> m >> start;

    // 간선 정보를 입력
    for (int i = 0; i < m; i++) {
        int a, b, c;
        cin >> a >> b >> c;
        // a번 노드에서 b번 노드로 가는 비용이 c
        graph[a].push_back({b, c});
    }

    // 최단 거리 테이블을 모두 무한으로 초기화
    fill(d, d + 100001, INF);
    
    // 다익스트라 알고리즘을 수행
    dijkstra(start);

    // 모든 노드로 가기 위한 최단 거리 출력
    for (int i = 1; i <= n; i++) {
        if (d[i] == INF)
            cout << "INFINITY" << ' ';
        else
            cout << d[i] << ' ';
    }
}


// 시간복잡도: O(ElogV)



/*
input example
6 11 1
1 2 2
1 3 5
1 4 1
2 3 3
2 4 2
3 2 3
3 6 5
4 3 3
4 5 1
5 3 1
5 6 2

output
0 2 3 1 2 4
*/