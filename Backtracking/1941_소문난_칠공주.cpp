#include <iostream>
#include <vector>
#include <algorithm>
#include <cstring>
using namespace std;

string arr[5];
int candidate[5][5];
bool visited[5][5];
int dx[] = {-1, 1, 0, 0};
int dy[] = {0, 0, -1, 1};
int result;

int dfs(int x, int y) {
	int cnt = 1;  // 방문한 노드 개수
	visited[x][y] = true;
	for (int i = 0; i < 4; i++) {
		int nx = x + dx[i];
		int ny = y + dy[i];
		if (nx < 0 || nx >= 5 || ny < 0 || ny >= 5)
			continue;
		// 방문하지 않은 후보일 경우 방문
		if (!visited[nx][ny] && candidate[nx][ny])
			cnt += dfs(nx, ny);
	}
	return cnt;
}


int main() {
	ios_base :: sync_with_stdio(0);
	cin.tie(0);

	for (int i = 0; i < 5; i++)
		cin >> arr[i];

	vector<int> temp(25, 0);
	for (int i = 0; i < 7; i++)
		temp[24 - i] = 1;  // 오름차순 정렬

	// 25명중에서 7명 뽑는 조합
	do {
		memset(candidate, 0, sizeof(candidate));
		int s_cnt = 0;
		int x, y;
		for (int i = 0; i < 25; i++) {
			candidate[i / 5][i % 5] = temp[i];
			if (temp[i] == 1 && arr[i / 5][i % 5] == 'S') {
				s_cnt++;
				x = i / 5;  // 이다솜파 친구 좌표 저장
				y = i % 5;
			}
		}

		if (s_cnt < 4)  // 이다솜파가 4명 미만일 경우
			continue;

		memset(visited, 0, sizeof(visited));
		if (dfs(x, y) == 7)  // 7명 모두 연결된 경우
			result++;
	} while (next_permutation(temp.begin(), temp.end()));

	cout << result << "\n";
} 
