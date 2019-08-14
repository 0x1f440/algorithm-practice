#include <iostream>
#include <algorithm>

using namespace std;

struct segment {
	int start, end;
};

bool compare(segment a, segment b) {
	if (a.start == b.start)
		return a.end < b.end;
	return a.start < b.start;
}

int main() {
	while (!cin.eof())
	{
		int m, idx = 0, ans = 0;
		segment segments[100003];

		cin >> m;
		cout << "¸ñÇ¥ : " << m << endl;

		while (true) {
			int s, e;
			cin >> s >> e;
			if (s > e) {
				int temp = s;
				s = e;
				e = temp;
			}

			if (s == 0 && e == 0)
				break;

			if (e < 0 || s > m || s == e)
				continue;

			segments[idx].start = s;
			segments[idx++].end = e;

		}

		sort(segments, segments + idx, compare);

		int i = 0, s = 0;
		while (true) {
			int max_end = 0, max_idx = -1;

			while (segments[i].start <= s && i < idx) {
				if (max_end <= segments[i].end) {
					max_end = segments[i].end;
					max_idx = i;
				}
				i++;
			}

			if (max_idx == -1) {
				cout << "0" << endl;
				break;
			}

			cout << segments[max_idx].start << ", " << segments[max_idx].end << endl;
			ans++;

			if (max_end >= m) {
				cout << ans << endl;
				break;
			}
			s = max_end;
		}
	}
	return 0;
}