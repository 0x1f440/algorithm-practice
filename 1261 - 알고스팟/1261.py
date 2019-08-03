import math
import sys
from heapq import *

sys.setrecursionlimit(100000)


class Node:
    def __init__(self):
        self.dist = math.inf
        self.visited = False
        self.blocked = False


def visit(_maze, x: int, y: int):
    if x == n-1 and y == m-1:
        print(maze[y][x].dist)
        exit(0)

    if not maze[y][x].visited:
        directions = [(x-1, y), (x, y-1), (x+1, y), (x, y+1)]

        for h, v in directions:
            if 0 <= h < n and 0 <= v < m and not maze[v][h].visited:
                maze[v][h].dist = min(maze[v][h].dist, maze[y][x].dist + maze[v][h].blocked)
                heappush(will_visit, [maze[v][h].dist, (h, v)])

        maze[y][x].visited = True

    _x, _y = heappop(will_visit)[1]
    visit(maze, _x, _y)


n, m = map(int, input().split())

maze = [[Node() for _ in range(n)] for _ in range(m)]
maze[0][0].dist = 0

will_visit = []

for i in range(len(maze)):
    for j, blocked in enumerate(input()):
        if blocked == '1':
            maze[i][j].blocked = True

visit(maze, 0, 0)

