import sys

nums = list(map(int, sys.stdin.readlines()[1].split()))
ans = [nums[0]]

for idx in range(1, len(nums)):
    temp = max(ans[idx-1]+nums[idx], nums[idx])
    ans.append(temp)

print(max(ans))
