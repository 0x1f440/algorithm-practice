import heapq
import sys

v = int(input()) + 1
graph = [{} for _ in range(v+1)]
visited = [False] * (v+1)
input = sys.stdin.readline

for _ in range(int(input())):
    x, y, value = map(int, input().split())
    if y in graph[x]:
        graph[x][y] = value if value < graph[x][y] else graph[x][y]
    else:
        graph[x][y] = value

will_visit = []
start, destination = map(int, input().split())
heapq.heappush(will_visit, (0, start))

while will_visit:
    dist, start = heapq.heappop(will_visit)
    if start == destination:
        print(dist)
        exit(0)
    visited[start] = True

    for edge in graph[start]:
        if visited[edge]:
            continue
        heapq.heappush(will_visit, (dist + graph[start][edge], edge))
