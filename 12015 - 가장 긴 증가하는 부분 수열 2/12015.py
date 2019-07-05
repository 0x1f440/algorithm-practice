import sys
from bisect import bisect_left

input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))
arr = [numbers[0]]

for num in numbers[1:]:
    if num > arr[-1]:
        arr.append(num)
    else:
        arr[bisect_left(arr, num)] = num

print(len(arr))