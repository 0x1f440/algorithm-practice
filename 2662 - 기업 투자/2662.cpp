#include <iostream>
#include <algorithm>
using namespace std;

int N, M;
int profit[303][23], dp[303][23], back[303][23], invest[23];

int main() {
	cin >> N >> M;

	for (int i = 1; i <= N; i++)
	{
		for (int j = 0; j <= M; j++)
			cin >> profit[i][j];
	}

	//profit[i][j]는 i원을 투자했을 때 j회사가 주는 수익금
	//dp[i][j] i원을 j번째 회사까지에 투자했을 때 얻을 수 있는 최대값
	for (int i = 1; i <= N; i++)
	{
		for (int j = 1; j <= M; j++)
		{
			for (int k = 0; k <= i; k++)
			{
				// 0 ~ i원을 j번째 회사에 투자한 경우.
				// [i-k]원을 [1]~[j-1]번째 회사에 재투자 가능
				if (dp[i][j] < profit[k][j] + dp[i - k][j - 1]) {
					dp[i][j] = profit[k][j] + dp[i - k][j - 1];
					back[i][j] = k;
				}
			}
		}
	}

	int i = N, j = M;
	while (j != 0) {
		if (back[i][j] != 0)
			invest[j] = back[i][j];

		i = i - back[i][j];
		j--;
	}


	cout << dp[N][M] << endl;
	for (int i = 1; i <= M; i++)
		cout << invest[i] << " ";

	return 0;
}