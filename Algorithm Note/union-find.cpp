#include <iostream>
using namespace std;

// 노드 개수, 간선(Union 연산) 개수
// 노드의 개수는 최대 100,000개라고 가정
int v, e;
int parent[100001]; // 부모 테이블

// 특정 원소가 속한 집합 찾기
int findParent(int x) {
	// 루트노드 찾을 때까지 재귀 호출
	if (x == parent[x]) return x;
	return parent[x] = findParent(parent[x]);
}

// 두 원소가 속한 집합 합치기
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

	// union 연산 수행
	for (int i = 0; i < e; i++) {
		int a, b;
		cin >> a >> b;
		unionParent(a, b);
	}

	// 각원소가 속한 집합 출력
	cout << "findParent: ";
	for (int i = 1; i <= v; i++)
		cout << findParent(i) << ' ';

	cout << '\n';

	// 부모 테이블 내용 출력
    cout << "parent: ";
    for (int i = 1; i <= v; i++)
        cout << parent[i] << ' ';

	cout << '\n';
}



/*
시간 복잡도
노드의 개수: V개
union 연산: 최대 V - 1개
find 연산: 최대 M개
=> 대략 O(V + MlogV)
*/


/*
input example
6 4
1 4
2 3
2 4
5 6

output
findParent: 1 1 1 1 5 5 
parent: 1 1 1 1 5 5
*/