# 시간초과
# C++로 다시 풀어보기로 함

import sys


def merge(left, right):
    result = []

    while left or right:
        if left and right:
            if left[0] > right[0]:
                result.append(left.pop(0))
            else:
                elem = right.pop(0)
                # 원래 등수가 더 낮았는데(배열의 뒤에 있었는데),
                # 자신의 앞 사람들과 비교했을 때 실력이 커서 앞지른 경우 앞지른 사람 수만큼 표시해줍니다
                elem[2] += len(left)
                result.append(elem)
        elif left:
            result.append(left.pop(0))
        else:  # right
            result.append(right.pop(0))

    return result


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


num = int(sys.stdin.readline())
nums = [[] for _ in range(num)]

# 인풋을 받아옵니다
for i in range(num):
    nums[i] = [int(sys.stdin.readline()), i + 1, 0]

merged = merge_sort(nums)

# 원래 순서대로 배치하고, 앞서나간 횟수만큼 원래 등수에서 빼서 출력합니다.
for i in merged:
    nums[i[1] - 1] = i[1] - i[2]

for i in nums:
    print(i)
