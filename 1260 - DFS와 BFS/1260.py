import sys
import collections


def dfs(graph: list, start: int):
    will_visit = collections.deque([start])
    visited = [False for _ in range(len(graph) + 1)]

    while will_visit:
        current = will_visit.pop()
        if visited[current]:
            continue

        visited[current] = True
        print(current, end=" ")

        for vertex in reversed(sorted(graph[current])):
            if not visited[vertex]:
                will_visit.append(vertex)
    print()


def bfs(graph: list, start: int):
    next_visit = collections.deque([start])
    visited = [False for _ in range(len(graph) + 1)]

    while next_visit:
        current = next_visit.popleft()
        visited[current] = True
        print(current, end=" ")

        for vertex in sorted(graph[current]):
            if not visited[vertex] and vertex not in next_visit:
                next_visit.append(vertex)
    print()


def main():
    vertex, edge, start_vertex = map(int, sys.stdin.readline().rstrip("\n").split())
    graph = [list() for _ in range(vertex + 1)]

    for _ in range(edge):
        start, end = map(int, sys.stdin.readline().rstrip("\n").split())
        graph[start].append(end)
        graph[end].append(start)

    dfs(graph, start_vertex)
    bfs(graph, start_vertex)


if __name__ == '__main__':
    main()
