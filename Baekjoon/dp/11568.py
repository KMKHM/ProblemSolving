import sys

input = sys.stdin.readline

n = int(input())

nums = list(map(int, input().split()))

dp = [0] * n

dp[0] = 1

for i in range(1, n):
    for j in range(i):
        if nums[i] <= nums[j]:
            continue
        dp[i] = max(dp[j] + 1, dp[i])

print(dp[-1])