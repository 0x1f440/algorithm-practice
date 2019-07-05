import heapq
import sys
import math


class Vertex:
    def __init__(self):
        self.edge = {}
        self.visited = False
        self.dist = math.inf

    def __lt__(self, other):
        return self.dist < other.dist


input = sys.stdin.readline
print = sys.stdout.write
vertices, edges = map(int, input().split())
graph = [Vertex() for _ in range(vertices + 1)]

will_visit = []
start_vertex = int(input())
graph[start_vertex].dist = 0
heapq.heappush(will_visit, (graph[start_vertex].dist, graph[start_vertex]))

for _ in range(edges):
    here, there, cost = map(int, input().split())
    if there in graph[here].edge:
        graph[here].edge[there] = cost if cost < graph[here].edge[there] else graph[here].edge[there]
    else:
        graph[here].edge[there] = cost

while will_visit:
    dist, vertex = heapq.heappop(will_visit)
    if vertex.visited:
        continue
    else:
        vertex.visited = True

    for edge in vertex.edge:
        if graph[edge].visited:
            continue

        graph[edge].dist = min(graph[edge].dist, dist + vertex.edge[edge])
        heapq.heappush(will_visit, (graph[edge].dist, graph[edge]))

for v in graph[1:]:
    print(f"{v.dist}\n" if v.dist is not math.inf else "INF\n")
