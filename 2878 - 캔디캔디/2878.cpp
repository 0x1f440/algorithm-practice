#include <iostream>
#include <algorithm>

using namespace std;

int candy, n, r, offset;
unsigned long long ans, request[100002];

int main() {
	cin >> candy >> n;
	for (int i = 0; i < n; i++)
	{
		cin >> request[i];
	}
	sort(request, request + n, greater<int>());

	while (candy > 0)
	{
		while (request[r] == request[r + 1])
			r++;

		offset = request[r] - request[r + 1];

		bool enough_candy = true;
		if (candy < offset * (r + 1))
			enough_candy = false;

		for (int i = 0; i <= r; i++)
		{
			if (enough_candy) {
				request[i] -= offset;
				candy -= offset;
			}
			else {
				request[i] -= 1;
				candy -= 1;
				if (candy == 0)
					break;
			}
		}
	}

	for (int i = 0; i < n; i++)
	{
		ans += request[i] * request[i];
	}

	cout << ans;
	return 0;
}