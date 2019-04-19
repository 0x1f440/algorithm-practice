# radix sort / 기수 정렬
# 각 자리수의 순서대로 정렬하는 것을 가장 큰 자리수만큼 반복한다
# stable sorting / 안정 정렬이다 (동일한 값에 대해 기존의 순서가 유지)
# in-place 알고리즘이다.
# 비교 연산을 하지 않는다
# O(dn) (d는 데이터의 최대 자리수)


def radix_lsd(arr):
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


def get_pos(arr, pos):
    position = pos

    if pos == 0:  # 맨 처음 호출 시 자리수를 계산합니다.
        for i in arr:
            if len(str(i)) > position:
                position = len(str(i))

        position = pow(10, position - 1)
        print("------------------------------")
        print("pos:", position, ", arr:", arr)

    return position


def radix_msd(arr, pos=0):
    position = get_pos(arr, pos)

    stack_list = [[] for _ in range(10)]

    for number in arr:  # 각 자릿수에 맞게 스택에 삽입
        div_num = number // position
        radix = div_num % 10
        stack_list[radix].append(number)

    print(stack_list)

    arr = []  # 재귀호출을 이용하여 정렬합니다
    for numbers in stack_list:
        if position >= 10 and numbers:
            arr += radix_msd(numbers, position // 10)
        else:
            arr += numbers

    return arr


test_case = [544, 4902, 392, 1000, 1, 2, 4355, 567, 565]
print("\n결과 : " + str(radix_msd(test_case)))
