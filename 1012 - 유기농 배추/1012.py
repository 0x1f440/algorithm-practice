import sys

sys.setrecursionlimit(5000)
farm = []
visited = []


def find_adjacent(_x, _y):
    if visited[_y][_x]:
        return 0

    visited[_y][_x] = True

    if not farm[_y][_x]:
        return 0

    will_visit = [(_y - 1 if _y - 1 > 0 else 0, _x), (_y, _x - 1 if _x - 1 > 0 else 0),
                  (_y + 1, _x), (_y, _x + 1)]

    for coordinate in will_visit:
        try:
            if farm[coordinate[0]][coordinate[1]]:
                find_adjacent(coordinate[1], coordinate[0])
        except:
            continue

    return 1


for _ in range(int(sys.stdin.readline())):
    result = 0
    x, y, pos = map(int, sys.stdin.readline().split())

    farm = [[False] * x for _ in range(y)]
    visited = [[False] * x for _ in range(y)]

    for _ in range(pos):
        _x, _y = map(int, sys.stdin.readline().split())
        farm[_y][_x] = True

    for _y in range(y):
        for _x in range(x):
            if visited[_y][_x]:
                continue

            if farm[_y][_x]:
                result += find_adjacent(_x, _y)

    sys.stdout.write(str(result)+"\n")
