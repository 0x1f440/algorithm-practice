import sys

goal = int(sys.stdin.readline().split()[1])
cards = sorted(map(int, sys.stdin.readline().split()))
max_sum = 0

for i, x in enumerate(cards):
    for j, y in enumerate(cards[i+1:]):
        sum = x+y
        for z in cards[i+j+2:]:
            if goal >= sum + z > max_sum:
                max_sum = sum + z

print(max_sum)