block = [1, 2, 4]

for i in range(3, 11):
	block.append(block[i - 3] + block[i - 2] + block[i - 1])

for i in range(int(input())):
	print(block[int(input()) - 1])