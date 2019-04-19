# insertion sort / 삽입 소트
# 각 반복에서 정렬되지 않은 나머지 부분 중 첫 번째 항목을 제거한 뒤
# 이미 정렬된 부분의 정확한 위치에 삽입된다.
# 같은 O(n^2) 알고리즘에 비교하여 빠르다
# 안정 정렬이다
# in-place 알고리즘이다.


def insertion_sort(arr):
    for i in range(1, len(arr)):
        # 첫 번째 원소는 이미 정렬되어 있는 것과 마찬가지기 때문에 두 번째 원소부터 시작
        print(str(i) + "번째 / 삽입될 원소 : " + str(arr[i]))
        for j in range(i):
            # 이미 정렬된 부분을 돌면서 자리를 찾는다
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

        print("결과 : " + str(arr))

    return arr


print("결과 : " + str(insertion_sort([2, 4, 6, 4, 7, 8, 3])))
