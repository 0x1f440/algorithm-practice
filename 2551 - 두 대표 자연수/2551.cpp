#include <iostream>
#include <algorithm>
using namespace std;

int n, m;
int nums[5000001];
int counter[10001];

int main() {
	cin >> n;
	long long all_sum = 0;

	for (int i = 0; i < n; i++) {
		int idx;
		cin >> idx;
		all_sum += idx;
		counter[idx]++;

		if (nums[i] > m)
			m = nums[i];
	}

	int idx = 0;
	for (int i = 0; i <= m; i++)
	{
		if (counter[i] > 0) {
			for (int j = 0; j < counter[i]; j++) {
				nums[idx++] = i;
			}
		}
	}

	int avg = all_sum / n;

	if (all_sum / n == (all_sum - 1) / n) {
		long long f_power_sum = 0, s_power_sum = 0;

		for (int i = 0; i < n; i++) {
			f_power_sum += abs(nums[i] - avg) * abs(nums[i] - avg);
			s_power_sum += abs(nums[i] - (avg + 1)) * abs(nums[i] - (avg + 1));
		}

		if (f_power_sum > s_power_sum)
			avg += 1;
	}

	cout << nums[(n - 1) / 2] << " " << avg;

	return 0;
}