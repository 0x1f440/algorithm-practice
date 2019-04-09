# quick sort / 퀵 정렬
# 임의의 피벗을 잡고 작거나 같은 수를 왼쪽으로, 큰 수를 오른쪽으로 보낸다.
# 위의 과정이 끝나면 왼쪽, 오른쪽 부분배열에 대해 똑같은 과정을 반복한다.
# 불안정 정렬
# O(nlogn), 최악의 경우 O(n^2)
# CPU 캐시의 히트율이 높도록 설계되어 있어 실질적으로는 nO(nlogn)보다 빠르다


def quick_sort(arr, start, end):
    if start < end:
        #  현재 리스트의 피벗을 구한다
        pivot = partition(arr, start, end)

        #  피벗을 기준으로 양 옆의 부분배열을 가지고 퀵소트 함수를 재귀호출한다
        quick_sort(arr, start, pivot - 1)
        quick_sort(arr, pivot + 1, end)

    return arr


def partition(value, start, end):
    print("피봇 : " + str(value[end]) + " / 정렬될 리스트 :" + str(value[start:end+1]))
    # 부분배열의 맨 끝을 피봇으로 정합니다
    pivot = end

    # 피봇을 기준으로 부분배열들을 재배치하고 피봇의 인덱스를 리턴
    wall = start
    left = start

    while left < pivot:
        if value[left] < value[pivot]:
            value[wall], value[left] = value[left], value[wall]
            wall += 1
        left += 1

    value[wall], value[pivot] = value[pivot], value[wall]
    pivot = wall

    print("부분 정렬된 리스트 : " + str(value))

    return pivot


test_case = list(map(int, input().split(',')))
print("인풋 : " + str(test_case), end="\n\n")
print("결과 : " + str(quick_sort(test_case, 0, len(test_case)-1)))
