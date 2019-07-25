#include <iostream>
#include <algorithm>

using namespace std;

int n, trees[1000001], goal;

int main() {
	cin >> n >> goal;
	for (int i = 0; i < n; i++) {
		cin >> trees[i];
	}

	sort(trees, trees + n);

	long long low = 0, mid, high = trees[n - 1], result = 0;

	while (low < high) {
		mid = low + ((high - low) / 2);

		long long sum = 0;
		int i = n;

		while (trees[--i] > mid) {
			sum += trees[i] - mid;
		}

		if (sum < goal) {
			high = mid;
		}
		else {
			result = mid;
			low = mid + 1;
		}
	}
	cout << result;


	return 0;
}
