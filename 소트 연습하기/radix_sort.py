# radix sort / 기수 정렬
# 각 자리수의 순서대로 정렬하는 것을 가장 큰 자리수만큼 반복한다
# stable sorting / 안정 정렬이다 (동일한 값에 대해 기존의 순서가 유지)
# in-place 알고리즘이다.
# 비교 연산을 하지 않는다
# O(dn) (d는 데이터의 최대 자리수)


def radix_sort(arr):
    position = 1

    while True:
        stack_list = [list() for _ in range(10)]
        is_sorted = True

        for number in arr:
            div_num = number // position
            radix = div_num % 10
            stack_list[radix].append(number)

            if div_num > 10:
                is_sorted = False

        print(stack_list)
        position *= 10
        arr.clear()

        for numbers in stack_list:
                for num in numbers:
                    arr.append(num)

        print(arr)
        print("------------------")

        if is_sorted:
            return arr


test_case = list(map(int, input().split(',')))
print("결과 : " + str(radix_sort(test_case)))
