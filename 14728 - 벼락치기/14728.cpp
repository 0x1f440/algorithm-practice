#include <iostream>
#include <algorithm>
using namespace std;

struct Subject {
	int time, score;
};

int N, T, dp[2][10001];
Subject subject[1001];

int main() {
	cin >> N >> T;

	for (int i = 0; i < N; i++)
		cin >> subject[i].time >> subject[i].score;

	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j <= T; j++)
		{
			if (j < subject[i].time)
				dp[i % 2][j] = dp[(i + 1) % 2][j];
			else
				dp[i % 2][j] = max(dp[(i + 1) % 2][j], subject[i].score + dp[(i + 1) % 2][j - subject[i].time]);
		}
	}

	cout << dp[(N - 1) % 2][T] << endl;

	return 0;
}