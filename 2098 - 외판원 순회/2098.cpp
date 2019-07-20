#include <iostream>
using namespace std;

int n;
int w[16][16];
int dp[16][1 << 16];

int tsp(int v, int mask) {
	// 1. ����� ������ �� �� �ž�!!!!!!
	if (dp[v][mask] != -1) {
		return dp[v][mask];
	}

	// 1.5. ���� ���� ����!!!!!!!!
	if (mask == 0) {
		// ���� v->0�� �� ����?�Ф�
		if (w[v][0] == 0) {
			return 20000000;
		}
		dp[v][mask] = w[v][0];
		return dp[v][mask];
	}

	// 2. ���� ���� v�� �ִµ� ��� �� �� ������?
	int min_cost = 99999999;
	for (int i = 0; i < n; i++) {
		int ith_mask = 1 << i;
		if (w[v][i] != 0 && (mask & ith_mask)) {
			// 3. �� ���� cost�� ���ϱ�?
			int cost = w[v][i] + tsp(i, mask - ith_mask);
			if (min_cost > cost) {
				min_cost = cost;
			}
		}
	}

	// 4. �׷��� ��������� dp[v][mask]�� ����?
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