#include <iostream>
using namespace std;

int n;
int w[16][16];
int dp[16][1 << 16];

int tsp(int v, int mask) {
	// 1. 계산을 했으면 안 할 거야!!!!!!
	if (dp[v][mask] != -1) {
		return dp[v][mask];
	}

	// 1.5. 가장 쉬운 문제!!!!!!!!
	if (mask == 0) {
		// 만약 v->0을 못 가면?ㅠㅠ
		if (w[v][0] == 0) {
			return 20000000;
		}
		dp[v][mask] = w[v][0];
		return dp[v][mask];
	}

	// 2. 나는 지금 v에 있는데 어디를 갈 수 있을까?
	int min_cost = 99999999;
	for (int i = 0; i < n; i++) {
		int ith_mask = 1 << i;
		if (w[v][i] != 0 && (mask & ith_mask)) {
			// 3. 그 때의 cost는 얼마일까?
			int cost = w[v][i] + tsp(i, mask - ith_mask);
			if (min_cost > cost) {
				min_cost = cost;
			}
		}
	}

	// 4. 그래서 결론적으로 dp[v][mask]는 뭐야?
	dp[v][mask] = min_cost;
	return dp[v][mask];
}

int main() {
	cin >> n;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			cin >> w[i][j];
		}
	}

	for (int i = 0;i < n;i++) {
		for (int j = 0;j < (1 << n);j++) {
			dp[i][j] = -1;
		}
	}

	cout << tsp(0, (1 << n) - 2) << endl;
	return 0;
}