import sys

input = sys.stdin.readline
users = [[] for _ in range(200)]

for _ in range(int(input())):
    age, name = input().rstrip().split()
    users[int(age)].append(name)

for age, names in enumerate(users):
    for name in names:
        print(f"{age} {name}")
