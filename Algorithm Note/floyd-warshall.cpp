/*
모든 노드에서 다른 모든 노드까지의 최단 경로 구하기
*/
#include <iostream>
#define INF 1e9
using namespace std;

// 노드 개수, 간선 개수
// 노드 최대 개수 500개 가정
int n, m;
// 최단 거리 테이블
int d[501][501];

int main() {
	cin >> n >> m;

	// 최단 거리 테이블 초기화
	for (int i = 0; i < 501; i++)
		fill(d[i], d[i] + 501, INF);

	// 자기 자신으로 가는 비용 초기화
	for (int i = 1; i <= n; i++)
		d[i][i] = 0;

	
    // 간선 정보 입력
    for (int i = 0; i < m; i++) {
        // a에서 b로 가는 비용 c
        int a, b, c;
        cin >> a >> b >> c;
        d[a][b] = c;
    }

	// 플로이드 워셜 알고리즘 수행
	for (int k = 1; k <= n; k++)
        for (int i = 1; i <= n; i++)
            for (int j = 1; j <= n; j++)
                d[i][j] = min(d[i][j], d[i][k] + d[k][j]);

	// 결과 출력
	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= n; j++) {
			if (d[i][j] == INF)
				cout << "INFINITY" << ' ';
			else
				cout << d[i][j] << ' ';
		}
		cout << '\n';
	}
}


// 시간 복잡도: O(N^3)


/*
input example
4 7
1 2 4
1 4 6
2 1 3
2 3 7
3 1 5
3 4 4
4 3 2

output
0 4 8 6 
3 0 7 9
5 9 0 4
7 11 2 0
*/