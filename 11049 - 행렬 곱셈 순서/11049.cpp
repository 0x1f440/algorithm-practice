#include <iostream>
#include <algorithm>
#include <climits>
using namespace std;

struct Matrix
{
	int r, c;
};

int N, dp[502][502];
Matrix m[502];

int get_sum(int s, int e) {
	if (s == e) return 0;

	if (dp[s][e] != INT_MAX) return dp[s][e];

	for (int i = s; i < e; i++) {
		int cost = get_sum(s, i) + get_sum(i + 1, e) + m[s].r * m[i].c * m[e].c;
		//if (dp[s][e]>cost)
		//	cout << "dp["<<s<<"]["<<e<<"] = dp[" <<s<<"]["<<i<<"]+dp["<<i+1<<"]["<<e<<"] +"<< m[s].r * m[i].c * m[e].c;
		dp[s][e] = min(dp[s][e], cost);

	}
	return dp[s][e];
}

int main() {
	cin >> N;
	for (int i = 0; i < N; i++)
		cin >> m[i].r >> m[i].c;

	for (int i = 0; i < N; i++)
		for (int j = 0; j < N; j++)
			dp[i][j] = INT_MAX;

	cout << get_sum(0, N - 1) << endl;

	//for (int i = 0; i < N; i++)
	//{
	//	for (int j = 0; j < N; j++)
	//		cout << dp[i][j] << " ";
	//	cout << endl;
	//}
	return 0;
}