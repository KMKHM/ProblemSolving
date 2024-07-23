"""
오렌지 출하
문제: https://www.acmicpc.net/problem/11985
"""
import sys

input = sys.stdin.readline

n, m, k = map(int, input().split())

# k + s * (b-a)

nums = [0] + [int(input()) for _ in range(n)]

dp = [sys.maxsize] * (n+1)
dp[0] = 0

for i in range(1, n+1):
    max_value, min_value = 0, sys.maxsize
    for j in range(1, m+1):
        if i < j:
            break

        max_value = max(max_value, nums[i-j+1])
        min_value = min(min_value, nums[i-j+1])
        dp[i] = min(dp[i], dp[i-j] + k + j * (max_value - min_value))

print(dp)



