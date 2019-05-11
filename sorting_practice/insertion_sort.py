# insertion sort / 삽입 소트
# 각 반복에서 정렬되지 않은 나머지 부분 중 첫 번째 항목을 제거한 뒤
# 이미 정렬된 부분의 정확한 위치에 삽입된다.
# 같은 O(n^2) 알고리즘에 비교하여 빠르다
# 안정 정렬이다
# in-place 알고리즘이다.


def insertion_sort_old(arr):
    for i in range(1, len(arr)):
        for j in range(i):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
                print(arr[:i])
        print("결과 : " + str(arr))

    return arr


def insertion_sort(arr):
    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            if arr[j-1] > arr[j]:
                arr[j-1], arr[j] = arr[j], arr[j-1]
                print(arr[:i])
        print("결과 : " + str(arr))

    return arr


print(" 최종결과 : " + str(insertion_sort([2, 4, 6, 4, 7, 8, 3])))
# 근데 결국 거의 똑같은 코드같아 보임
# 새 배열을 만들어서 넣을까 했는데 거기도 하나하나 넣으면서 원소들이 밀리는 거는 똑같음
# 더 이상 최적화 어떻게 하죠?