#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

/* 선택 정렬 */
void sel_sort(int n, int arr[]) {
	for(int i = 0; i < n; i++) {
		int min_idx = i;
		for (int j = i + 1; j < n; j++)
			if (arr[j] < arr[min_idx])
				min_idx = j;
		swap(arr[i], arr[min_idx]);
	}
}

// 시간복잡도: O(N^2)


/* 삽입 정렬 */
void ins_sort(int n, int arr[]) {
	for (int i = 1; i < n; i++)
		for (int j = i; j > 0; j--) {
			if (arr[j] < arr[j - 1])  // 한 칸씩 왼쪽으로 이동
				swap(arr[j], arr[j - 1]);
			else  // 자신보다 작은 수를 만나면 멈춤
				break;
		}
}

// 시간복잡도: O(N^2)
// 최선의 경우: O(N)


/* 퀵 정렬 */
void quick_sort(int arr[], int start, int end) {
	if (start >= end)  // 원소가 1개인 경우 종료
		return;
	int pivot = start;
	int left = start + 1;
	int right = end;
	while (left <= right) {
		// 피벗보다 큰 데이터를 찾을 때까지 반복
		while (left <= end && arr[left] <= arr[pivot])
			left++;
		// 피벗보다 작은 데이터를 찾을 때까지 반복
		while (right > start && arr[right] >= arr[pivot])
			right--;
		// 엇갈렸다면 작은 데이터와 피벗을 교체
		if (left > right)
			swap(arr[pivot], arr[right]);
		// 엇갈리지 않았다면 작은 데이터와 큰 데이터 교체
		else
			swap(arr[left], arr[right]);
		// 피벗을 기준으로 분할 후 각각 정렬 수행
		quick_sort(arr, start, right - 1);
		quick_sort(arr, right + 1, end);

	}
}

// 평균 시간복잡도: O(NlogN)
// 최악의 경우: O(N^2)


/* 계수 정렬 */
#define MAX_VALUE 9  // 배열 내 최대값
// 모든 범위를 포함하는 배열 선언
int cnt[MAX_VALUE + 1];

void count_sort(int n, int arr[]) {
	for (int i = 0; i < n; i++)
		cnt[arr[i]]++;  // 각 데이터에 해당하는 인덱스 값 증가
	
	for (int i = 0; i <= MAX_VALUE; i++)
		for (int j = 0; j < cnt[i]; j++)
			cout << i << ' ';  // 값이 등장한 횟수만큼 출력
}

// 시간복잡도: O(N + K)
// N: 데이터의 개수
// K: 데이터의 최댓값


/* sort() 함수 */
// 내림차순 정렬을 위한 비교 함수
bool desc(int a, int b) {
	return a > b;
}

void sort_prac() {
	int n = 15;
	int arr[15] = {7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2};

	sort(arr, arr + n);  // 오름차순 정렬
	for (int i = 0; i < n; i++)
		cout << arr[i] << ' ';

	cout << '\n';

	sort(arr, arr + n, desc);  // 내림차순 정렬
	// sort(arr, arr + n, greater<int>());
	for (int i = 0; i < n; i++)
		cout << arr[i] << ' ';
}

// 성적 내림차순 후 이름 오름차순 정렬
bool compare(pair<char, int> p1, pair<char, int> p2) {
	if(p1.second == p2.second)
		return p1.first < p2.first;
	return p1.second > p2.second;
}

void pair_sort() {
	vector<pair<char, int>> v;
	v.push_back(make_pair('a', 80));
	v.push_back(make_pair('b', 100));
	v.push_back(make_pair('c', 80));
	v.push_back(make_pair('d', 90));

	sort(v.begin(), v.end(), compare);
	for (int i = 0; i < v.size(); i++)
		cout << v[i].first << ' ' << v[i].second << '\n';
}


int main() {
	int n = 15;
	int arr[15] = {7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2};
	quick_sort(arr, 0, n - 1);
	for (int i = 0; i < n; i++)
		cout << arr[i] << ' ';
}