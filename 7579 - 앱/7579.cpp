#include <iostream>
#include <algorithm>
#include <climits>

using namespace std;

struct App
{
	int memory, cost;
};

bool compare(App a, App b) {
	return a.cost < b.cost;
}

App apps[101];
int N, M, dp[2][100002], max_cost, ans = INT_MAX;

int main() {
	cin >> N >> M;

	for (int i = 1; i <= N; i++)
		cin >> apps[i].memory;

	for (int i = 1; i <= N; i++)
	{
		cin >> apps[i].cost;
		max_cost += apps[i].cost;
	}

	sort(apps + 1, apps + N + 1, compare);

	// dp[i][j]는 i번째 app까지를 고려했을 때, cost로 확보할 수 있는 메모리의 최대값
	for (int i = 1; i <= N; i++)
	{
		for (int j = 0; j <= max_cost; j++)
		{
			if (apps[i].cost > j)
				dp[i % 2][j] = dp[(i + 1) % 2][j];
			else
				dp[i % 2][j] = max(dp[(i + 1) % 2][j], dp[(i - 1) % 2][j - apps[i].cost] + apps[i].memory);

			if (dp[i % 2][j] >= M) {
				ans = min(ans, j);
			}
		}
	}
	cout << ans << endl;

	return 0;
}