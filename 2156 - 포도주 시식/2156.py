n = int(input())
if n == 1:
    print(input())
    exit(0)

wine = [int(input()) for _ in range(n)]

dp = [[0, 0, 0, 0] for _ in range(n)]
dp[1][0], dp[1][1], dp[1][2], dp[1][3] = sum(wine[0:2]), wine[0], wine[1], 0

for i in range(2, n):
    dp[i][0] = dp[i - 1][2] + wine[i]   # [1, 1]
    dp[i][1] = dp[i - 1][0] if dp[i - 1][0] > dp[i - 1][2] else dp[i - 1][2]  # [1, 0]
    dp[i][2] = dp[i - 1][1] + wine[i] if dp[i - 1][1] + wine[i] > dp[i - 1][3] + wine[i] else dp[i - 1][3] + wine[i]  # [0, 1]
    dp[i][3] = dp[i - 1][1]  # [0, 0]

print(max(dp[n - 1]))