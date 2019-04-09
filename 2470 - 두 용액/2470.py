import sys
num = int(sys.stdin.readline())
solutes = sorted(list(map(int, sys.stdin.readline().split()))[:num])
min_diff = (abs(solutes[0] + solutes[1]), solutes[0], solutes[1])


def binary_search(idx, val):
    start = idx + 1
    end = len(solutes) - 1

    while start < end:
        mid = (start + end) // 2

        if mid == start or mid >= end:
            break

        if solutes[mid] < val:
            start = mid
        elif solutes[mid] > val:
            end = mid
        else:  # mid == val
            print(-val, solutes[mid])
            exit(0)
    return start, end


for i in range(len(solutes)-1):
    s, e = binary_search(i, -solutes[i])

    diff_s = abs(solutes[i] + solutes[s])
    diff_e = abs(solutes[i] + solutes[e])

    if min_diff[0] > min(diff_s, diff_e):
        if diff_s < diff_e:
            min_diff = (diff_s, solutes[i], solutes[s])
        else:
            min_diff = (diff_e, solutes[i], solutes[e])

print(*min_diff[1:])
