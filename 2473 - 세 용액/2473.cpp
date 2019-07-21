#include <iostream>
#include <algorithm>

using namespace std;

long long solutions[5000], current_sum;
int n, result_idx[3];
int high, low, mid;

void print_result() {
	cout << solutions[result_idx[0]] << " " << solutions[result_idx[1]] << " " << solutions[result_idx[2]];
	exit(0);
}

void set_result(int a, int b, int c, long long sum) {
	result_idx[0] = a;
	result_idx[1] = b;
	result_idx[2] = c;
	current_sum = sum;
}

void binary_search(int _idx, int idx, long long query) {
	low = idx + 1;
	high = n - 1;

	while (low < high) {
		mid = (low + high) / 2;

		if (mid <= low || high <= mid)
			break;

		if (solutions[mid] < query) {
			low = mid;
		}
		else if (query < solutions[mid]) {
			high = mid;
		}
		else {
			set_result(_idx, idx, mid, 0);
			print_result();
		}
	}

	long long temp1 = abs(solutions[_idx] + solutions[idx] + solutions[low]);
	long long temp2 = abs(solutions[_idx] + solutions[idx] + solutions[high]);

	if (min(temp1, temp2) < current_sum) {
		if (temp1 < temp2)
			set_result(_idx, idx, low, temp1);
		else
			set_result(_idx, idx, high, temp2);
	}
}

int main() {
	// i번째를 고르고 i+1부터 끝까지 바이너리 서치로 i랑 가장 가까운 조합을 찾자
	// 아마 N*NlogN

	cin >> n;
	for (int i = 0; i < n; i++)
		cin >> solutions[i];

	sort(solutions, solutions + n);
	set_result(0, 1, 2, abs(solutions[0] + solutions[1] + solutions[2]));

	for (int i = 0; i < n - 2; i++) {
		for (int j = i + 1; j < n - 1; j++) {
			// 첫번째 solution + 두번째 solution과 더해서 가장 0과 가까워야 하기 때문에 -를 붙임
			long long query = -(solutions[i] + solutions[j]);
			binary_search(i, j, query);
		}
	}
	print_result();

	return 0;
}
