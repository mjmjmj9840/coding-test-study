#include <iostream>
#include <vector>
#include <queue>
using namespace std;

bool visited[9];
vector<int> graph[9];

void bfs(int start) {
	queue<int> q;
	// 시작 노드를 큐에 넣고 방문 처리
	q.push(start);
	visited[start] = true;

	while (!q.empty()) {
		int x = q.front();
		q.pop();
		cout << x << ' ';
		// 연결된 노드 중 방문 안한 노드 큐에 넣고 방문 처리
		for (int i = 0; i < graph[x].size(); i++) {
			int y = graph[x][i];
			if (!visited[y]) {
				q.push(y);
				visited[y] = true;
			}
		}
	}
}

int main() {
	// 노드 1에 연결된 노드 정보 저장 
    graph[1].push_back(2);
    graph[1].push_back(3);
    graph[1].push_back(8);
    
    // 노드 2에 연결된 노드 정보 저장 
    graph[2].push_back(1);
    graph[2].push_back(7);
    
    // 노드 3에 연결된 노드 정보 저장 
    graph[3].push_back(1);
    graph[3].push_back(4);
    graph[3].push_back(5);
    
    // 노드 4에 연결된 노드 정보 저장 
    graph[4].push_back(3);
    graph[4].push_back(5);
    
    // 노드 5에 연결된 노드 정보 저장 
    graph[5].push_back(3);
    graph[5].push_back(4);
    
    // 노드 6에 연결된 노드 정보 저장 
    graph[6].push_back(7);
    
    // 노드 7에 연결된 노드 정보 저장 
    graph[7].push_back(2);
    graph[7].push_back(6);
    graph[7].push_back(8);
    
    // 노드 8에 연결된 노드 정보 저장 
    graph[8].push_back(1);
    graph[8].push_back(7);
    
    bfs(1);
}

/*
output: 1 2 3 8 7 4 5 6
시간 복잡도: O(V + E)
*/