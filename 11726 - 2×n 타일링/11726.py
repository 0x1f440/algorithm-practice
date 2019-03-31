n = int(input())
block = [1, 2]
result = 2

if n <= 2:
	print(block[n - 1])
	exit(0)

for i in range(n - 2):
	result = (result + block[0]) % 10007
	block[0] = block[1]
	block[1] = result

print(result)
