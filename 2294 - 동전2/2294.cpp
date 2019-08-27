#include <iostream>
#include <algorithm>
using namespace std;

int n, k, coins[101], dp[10001];

int main() {
	cin >> n >> k;
	for (int i = 0; i < n; i++)
		cin >> coins[i];

	for (int i = 1; i <= k; i++)
		dp[i] = -1;

	for (int i = 0; i < n; i++)
	{
		for (int j = coins[i]; j <= k; j++)
		{
			if (dp[j - coins[i]] != -1)
				if (dp[j] == -1)
					dp[j] = dp[j - coins[i]] + 1;
				else
					dp[j] = min(dp[j], dp[j - coins[i]] + 1);
		}
	}

	cout << dp[k];

	return 0;
}