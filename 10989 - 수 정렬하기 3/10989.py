import sys

counter = [0]*10001

for _ in range(int(sys.stdin.readline())):
    counter[int(sys.stdin.readline())] += 1

for i in range(len(counter)):
    for j in range(counter[i]):
        print(i)
