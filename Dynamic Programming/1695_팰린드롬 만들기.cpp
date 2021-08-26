// 1695번: 팰린드롬 만들기

#include <iostream>
#include <cstring>
#include<algorithm>
using namespace std;

const int MAX = 5001;
int n;
int arr[MAX];
int dp[MAX][MAX]; // i부터 j까지 팰린드롬으로 만들기 위한 최소 개수

int makePalindrome(int i, int j) {
	if (i >= j)
		return 0;

	int& result = dp[i][j];

	if (result != -1)
		return result;

	if (arr[i] == arr[j])
		result = makePalindrome(i + 1, j - 1);
	else
		// arr[i]를 추가하거나 arr[j]를 추가하는 것 중에서 최솟값 고르기
		result = min(makePalindrome(i + 1, j), makePalindrome(i, j - 1)) + 1;

	return result;
}

int main() {
	ios_base :: sync_with_stdio(0);
	cin.tie(0);
	cin >> n;
	for(int i = 0; i < n; i++)
		cin >> arr[i];

	memset(dp, -1, sizeof(dp));

	cout << makePalindrome(0, n - 1) << '\n';
} 
