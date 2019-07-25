#include <iostream>
#include <queue>

using namespace std;
queue <int> que;

int dist[1000010];

int main() {
	int F, S, G, U, D;
	cin >> F >> S >> G >> U >> D;

	for (int i = 1; i <= F; i++)
		dist[i] = -1;

	dist[S] = 0;

	que.push(S);

	int current;
	while (!que.empty()) {
		current = que.front();
		que.pop();

		if (current == G) {
			//@TODO: ���� ���?!
			cout << dist[current] << endl;
			exit(0);
		}

		//@TODO: �ö󰡱� (����)
		if (current + U <= F && dist[current + U] == -1) {
			dist[current + U] = dist[current] + 1;
			que.push(current + U);
		}
		//@TODO: �������� (����)
		if (current - D >= 1 && dist[current - D] == -1) {
			dist[current - D] = dist[current] + 1;
			que.push(current - D);
		}

	}
	cout << "use the stairs" << endl;
	return 0;
}