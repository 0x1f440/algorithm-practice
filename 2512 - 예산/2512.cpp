#include <iostream>
#include <algorithm>

using namespace std;

int n;
long long request[10001], budget;

int main() {
	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> request[i];
	}
	cin >> budget;

	sort(request, request + n);

	long long low = 0, mid, high = request[n - 1], result = 0;

	while (low <= high) {
		mid = low + ((high - low) / 2);

		long long temp_sum = 0;

		for (int i = 0; i < n; i++) {
			temp_sum += min(mid, request[i]);
		}

		if (temp_sum <= budget) {
			result = mid;
			low = mid + 1;
		}
		else if (temp_sum > budget) {
			high = mid - 1;
		}
	}
	cout << result;


	return 0;
}
