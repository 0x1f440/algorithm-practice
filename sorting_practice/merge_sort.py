# merge sort / 합병 정렬
# 리스트를 1개의 원소가 될 때까지 쪼갠 후 정렬해 가며 합병한다.
# 안정 정렬
# 분할 정복 알고리즘의 하나이다


def merge_sort(arr):
    print("merge_sort called, argument is " + str(arr))

    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    print("left : " + str(left), end=" // ")
    print("right : " + str(right), end="\n\n")

    return merge(left, right)


def merge(left, right):
    result = []
    print("merging list...")

    while left or right:
        print("left " + str(left) + " // right " + str(right))
        if left and right:
            result.append(left.pop(0) if left[0] < right[0] else right.pop(0))
        elif left:
            result.append(left.pop(0))
        else:  # right
            result.append(right.pop(0))

    print("merge result... " + str(result), end="\n\n")
    return result


test_case = list(map(int, input().split(',')))

print("input was " + str(test_case), end="\n\n")
print("merge : " + str(merge_sort(test_case)))

