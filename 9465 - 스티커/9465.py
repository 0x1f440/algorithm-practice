for _ in range(int(input())):

	n = int(input())
	score = [[0]*3 for _ in range(n)]
	sticker = [[], []]

	for i in range(2):
		sticker[i] = list(map(int, input().split()))

	score[0] = [0, sticker[0][0], sticker[1][0]]

	for i in range(1, n):
		score[i][0] = score[i-1][1] if score[i-1][1] > score[i-1][2] else score[i-1][2]
		score[i][1] = score[i-1][2] + sticker[0][i] if score[i-1][2] > score[i-1][0] else score[i-1][0] + sticker[0][i]
		score[i][2] = score[i-1][1] + sticker[1][i] if score[i-1][1] > score[i-1][0] else score[i-1][0] + sticker[1][i]

	print(max(score[n-1]))