# insertion sort / 삽입 소트
# 각 반복에서 정렬되지 않은 나머지 부분 중 첫 번째 항목을 제거한 뒤
# 이미 정렬된 부분의 정확한 위치에 삽입된다.
# 같은 O(n^2) 알고리즘에 비교하여 빠르다
# 안정 정렬이다
# in-place 알고리즘이다.


def insertion_sort_old(arr):
    for i in range(1, len(arr)):
        # 첫 번째 원소는 이미 정렬되어 있는 것과 마찬가지기 때문에 두 번째 원소부터 시작
        print(f"{i}번째 / 삽입될 원소 : {arr[i]}")
        for j in range(i):
            # 이미 정렬된 부분을 돌면서 자리를 찾는다
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

        print("결과 : " + str(arr))

    return arr


def insertion_sort(arr):
    for i in range(1, len(arr)):
        print(f"넣을 원소 : {arr[i]}")
        value_to_insert = arr[i]
        index_to_insert = i

        for j in reversed(range(i)):
            if arr[j] <= value_to_insert:
                break

            arr[j+1] = arr[j]
            index_to_insert = j

        arr[index_to_insert] = value_to_insert

        print(f"정렬된 배열 : {arr[:i]}")

    return arr


print("최종결과 : ", insertion_sort([4, 4, 3, 1, 0, 2, 1, 6, 5, 7, 8]))
