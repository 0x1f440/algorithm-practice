fib = [0, 1, 1]
result = 0

n = int(input())

if n <= 2:
	print(fib[n])
	exit(0)

for i in range(n-1):
	fib[2] = (fib[0] + fib[1])
	fib[0], fib[1] = fib[1], fib[2]

print(fib[2])