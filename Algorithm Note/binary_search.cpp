#include <iostream>
#include <vector>
using namespace std;

/* 재귀함수로 구현한 이진 탐색 */
int binarySearch(vector<int>& arr, int target, int start, int end) {
	if (start > end) return -1;
	int mid = (start + end) / 2;
	if (arr[mid] < target)
		return binarySearch(arr, target, start + 1, end);
	else if (arr[mid] > target)
		return binarySearch(arr, target, start, mid - 1);
	else
		return mid;
}


/* 반복문으로 구현한 이진 탐색 */
int binarySearch2(vector<int>& arr, int target, int start, int end) {
	while (start <= end) {
		int mid = (start + end) / 2;
		if (arr[mid] < target)
			start = mid + 1;
		else if (arr[mid] > target)
			end = mid - 1;
		else
			return mid;
	}
	return -1;
}


int main() {
	vector<int> arr = {1, 3, 5, 7, 9, 11, 13, 15, 17, 19};
	int target = 9;

	int idx = binarySearch2(arr, target, 0, arr.size() - 1);
	cout << idx << '\n';
}