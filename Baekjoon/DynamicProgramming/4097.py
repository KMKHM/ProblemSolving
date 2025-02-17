"""
수익
문제: https://www.acmicpc.net/problem/4097
"""
nums = [0] + [-3,
4,
9,
-2,
-5,
8]

n = len(nums)

dp = [-10000] * (n)
dp[0] = 0

for i in range(1, n):
    for j in range(i):
        dp[i] = max(dp[j] + nums[i], dp[i])

print(dp)
