# selection sort / 선택 소트
# 아직 정렬되지 않은 값 중 가장 작은/큰 값을 선택하여
# 맞는 인덱스의 원소와 교환함


def selection_sort(arr):
    for i in range(len(arr)): 
        min_val = arr[i]
        min_index = i

        for j in range(i, len(arr)):
            if arr[j] < min_val:
                min_val = arr[j]
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


test_case = list(map(int, input().split(',')))
print("selection : " + str(selection_sort(test_case)))
