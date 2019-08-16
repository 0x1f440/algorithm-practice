#include <iostream>
#include <algorithm>

using namespace std;
long long cut[10002], L, ans_len = -1, ans_first;
int K, C;

bool is_valid(long long query) {
	int temp_idx = -1, c = 0;
	long long temp_len = -1, right = L;

	for (int i = 1; i < K - 1; i++)
	{
		if (right - cut[i] <= query) {
			if (right - cut[i + 1] <= query)
				continue;

			c++;
			temp_idx = i;
			temp_len = max(temp_len, right - cut[i]);
			right = cut[i];
		}
	}

	if (c > C || right > query)
		return false;

	temp_len = max(temp_len, right);

	if (c < C)
		temp_idx = K - 2;

	if (ans_len == -1 || ans_len > temp_len) {
		ans_len = temp_len;
		ans_first = cut[temp_idx];
	}
	else if (ans_len == temp_len) {
		ans_first = min(ans_first, cut[temp_idx]);
	}

	return true;
}

int main() {
	cin >> L >> K >> C;
	K += 2;

	for (int i = 1; i < K - 1; i++)
		cin >> cut[i];

	cut[K - 1] = L;
	sort(cut, cut + K, greater<long long>());

	long long s = 0, e = L, mid;
	while (s < e)
	{
		mid = s + (e - s) / 2;

		if (is_valid(mid))
			e = mid;
		else
			s = mid + 1;
	}

	cout << ans_len << " " << ans_first;
	return 0;
}