#include <iostream>
#include <algorithm>

using namespace std;
int N, ans;

struct Flower {
	int start, end;
};

bool compare(Flower a, Flower b) {
	if (a.start == b.start)
		return a.end < b.end;
	return a.start < b.start;
}

Flower flower[1000002];

int main() {
	cin >> N;

	int temp1, temp2, idx = 0;
	for (int i = 0; i < N; i++)
	{
		cin >> temp1 >> temp2;
		flower[idx].start = temp1 * 100 + temp2;
		cin >> temp1 >> temp2;
		flower[idx].end = temp1 * 100 + temp2;

		if (flower[idx].start != flower[idx].end && (flower[idx].start <= 1130 && flower[idx].end >= 301))
			idx++;
	}

	N = idx;
	sort(flower, flower + N, compare);

	int start = 301, end = 301;
	idx = 0;

	while (start <= 1130) {
		while (flower[idx].start <= start && idx < N) {
			end = max(end, flower[idx++].end);
		}
		if (start == end) {
			cout << "0" << endl;
			exit(0);
		}
		start = end;
		ans++;
	}
	cout << ans << endl;

	return 0;
}
