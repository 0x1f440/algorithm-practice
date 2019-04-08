# TODO
# 배열에 존재하는 값보다 더 크거나 작은 값을 검색할 때 에러가 납니다 


def binary_search(arr, num):
    start, end = 0, len(arr) - 1
    print("list : " + str(arr))

    while start <= end:
        mid = (start + end) // 2

        if num < arr[mid]:
            end = mid - 1

        elif num > arr[mid]:
            start = mid + 1

        else:
            print("index : " + str(mid))
            return mid

    print(str(start) + " / " + str(mid) + " / " + str(end))
    print("upper_bound : " + str(arr[start]) + " / lower_bound : " + str(arr[end]))


binary_search([-50, -30, 2, 3, 10, 40, 60, 90, 100, 105], -888)
