"""
가장 긴 짝수 연속한 부분 수열 (small)
문제: https://www.acmicpc.net/problem/22857
"""
import sys

input = sys.stdin.readline

n, k = map(int, input().split())

nums = list(map(int, input().split()))

dp = [0] * n
dp[0] = 1 if nums[0] % 2 == 0 else 0

for i in range(1, n):
    if dp[i-1] and nums[i] % 2 == 0:
        dp[i] = dp[i-1] + 1
    elif dp[i-1] and nums[i] % 2 != 0:
        continue
    elif not dp[i-1] and nums[i] % 2 == 0:
        dp[i] = 1

print(dp)

