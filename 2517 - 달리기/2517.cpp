#include <iostream>
using namespace std;

int n;

struct Athlete {
	int rank;
	int power;
	int potential;
};

int result[500050];
Athlete a[500050];
Athlete tmp[500050];

void get_potential(int s, int e) {
	if (s == e)	return;
	int p = s + (e - s) / 2;

	get_potential(s, p);
	get_potential(p + 1, e);

	int l = s, r = p + 1;

	for (int i = s; i <= e; i++) {
		if (l > p)
			tmp[i] = a[r++];
		else if (r > e)
			tmp[i] = a[l++];
		else {
			if (a[l].power > a[r].power) {
				a[r].potential += p - l + 1;
				tmp[i] = a[r++];
			}
			else {
				tmp[i] = a[l++];
			}
		}
	}

	for (int i = s; i <= e; i++)
		a[i] = tmp[i];
}

int main() {
	cin >> n;
	for (int i = 0; i < n; i++) {
		int power;
		cin >> power;
		a[i].rank = i;
		a[i].power = power;
	}

	get_potential(0, n - 1);

	for (int i = 0; i < n; i++)
		result[a[i].rank] = a[i].potential + 1;

	for (int i = 0; i < n; i++)
		cout << result[i] << "\n";

	return 0;
}