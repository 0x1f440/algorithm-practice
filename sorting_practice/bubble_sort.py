#  bubble sort / 거품 정렬
#  두 개의 인접한 원소를 검사하여 정렬한다.
#  O(n^2)


def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(1, len(arr) - i):
            if arr[j - 1] > arr[j]:
                arr[j - 1], arr[j] = arr[j], arr[j - 1]
        print(str(i) + "회차 결과 : " + str(arr))
    return arr


test_case = list(map(int, input().split(',')))
print("결과 : " + str(bubble_sort(test_case)))
