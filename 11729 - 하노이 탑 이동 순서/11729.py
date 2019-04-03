#  그 유명한 하노이 문제가 이렇게 이해 안 될 일인가?
start, mid, end = 1, 2, 3

n = int(input())
print(pow(2, n)-1)


def move_disk(n, start, mid, end):
	if n == 1:
		print(str(start) + " " + str(end))
		return

	# 1: n - 1개 원판을 시작막대서 도착 막대를 거쳐 중간 막대로
	move_disk(n - 1, start, end, mid)
	# 2: 시작 막대의 마지막 남은 1개 원판을 도착지 막대로
	print(str(start) + " " + str(end))
	# 3: 중간 막대로 옮긴 n-1개 원판을 다시 도착지 막대로
	move_disk(n - 1, mid, start, end)


move_disk(n, start, mid, end)
