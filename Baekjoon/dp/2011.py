"""
암호 코드
문제: https://www.acmicpc.net/problem/2011
"""
import sys

nums = list(map(int, input().rstrip()))

if nums[0] == 0:
    print(0)
    sys.exit(0)

n = len(nums)

dp = [0] * (n+1)
dp[0] = dp[1] = 1

for i in range(1, n):
    k = i+1
    if nums[k] > 0:
        dp[i] += dp[i-1]

    if 10<= nums[k] + nums[k-1] * 10 <= 26:
        dp[i] += dp[i-2]

print(dp[n] % 1000000)