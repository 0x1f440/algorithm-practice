n = int(input())
numbers = list(map(int, input().split()))
dp = [1]

for i in range(1, n):
	max_len = 0
	for j in range(i):
		if numbers[j] < numbers[i]:
			max_len = dp[j] if dp[j] > max_len else max_len
	dp.append(max_len + 1)

print(max(dp))
