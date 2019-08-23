#include <iostream>
#include <algorithm>

using namespace std;

int rgb[1001][3];
int N, temp;

int main() {
	cin >> N;
	int R, G, B;
	for (int i = 1; i <= N; i++)
	{
		cin >> R >> G >> B;
		rgb[i][0] = min(rgb[i - 1][1], rgb[i - 1][2]) + R;
		rgb[i][1] = min(rgb[i - 1][0], rgb[i - 1][2]) + G;
		rgb[i][2] = min(rgb[i - 1][0], rgb[i - 1][1]) + B;
	}
	cout << min(rgb[N][0], min(rgb[N][1], rgb[N][2]));
	return 0;
}

