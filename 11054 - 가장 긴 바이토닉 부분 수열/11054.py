n = int(input())
arr = list(map(int, input().split()))
dp_asc = [1 for _ in range(n)]
dp_desc = [1 for _ in range(n)]

for i in range(1, n):
    for j in range(i):
        if arr[j] < arr[i]:
            dp_asc[i] = max(dp_asc[j]+1, dp_asc[i])

        elif arr[j] > arr[i]:
            dp_desc[i] = max(dp_desc[j]+1, dp_asc[j]+1, dp_desc[i])

print(max(max(dp_asc), max(dp_desc)))