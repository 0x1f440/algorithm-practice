#include <iostream>

using namespace std;

int counter = 0;
int row = 0, col = 0;
int N, R, C;

void visit(int n, int r, int c) {
	//1. 2^1이 아니라면 2^(N-1)로 visit()를 호출 (4등분 하는 것임)
	//cout << n << ", (" << r << "," << c << ")" << endl;
	if (n == 0) {
		cout << counter;
		exit(0);
	}

	n -= 1;
	int starting_points[4][2] = {{r, c}, {r, c + (1 << n)}, {r + (1 << n), c}, {r + (1 << n), c + (1 << n)} };

	for (int i = 0; i < 4; i++)
	{
		if (R < starting_points[i][0] + (1 << n) && C < starting_points[i][1] + (1 << n)) {
			visit(n, starting_points[i][0], starting_points[i][1]);
		}
		else {
			int count = 1 << (2 * n);
			counter += count;
		}
	}
}

int main() {
	cin >> N >> R >> C;
	visit(N, 0, 0);

	return 0;
}
