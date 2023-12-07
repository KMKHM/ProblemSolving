"""
포도주 시식
문제: https://www.acmicpc.net/problem/2156
"""
import sys

input = sys.stdin.readline

n = int(input())

nums = [0] + [int(input()) for _ in range(n)]


if n == 1:
    print(nums[1])
elif n == 2:
    print(nums[1] + nums[2])
else:
    dp = [0] * (n + 1)

    dp[1] = nums[1]
    dp[2] = nums[1] + nums[2]

    for i in range(3, n+1):
        case1 = dp[i-3] + nums[i-1] + nums[i]
        case2 = dp[i-2] + nums[i]
        case3 = dp[i-1]
        dp[i] = max(case1, case2, case3)

    print(dp[-1])

