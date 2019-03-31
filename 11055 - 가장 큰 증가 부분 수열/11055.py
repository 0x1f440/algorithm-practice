n = int(input())
numbers = list(map(int, input().split()))
dp = [numbers[0]]

for i in range(1, n):
	max_val = 0

	for j in range(i):
		if numbers[j] < numbers[i]:
			max_val = dp[j] if dp[j] > max_val else max_val
	dp.append(max_val + numbers[i])

print(sorted(dp)[-1])