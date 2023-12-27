"""
민균이의 계략
문제: https://www.acmicpc.net/problem/11568
"""
import sys

input = sys.stdin.readline

n = int(input())

nums = list(map(int, input().split()))

dp = [1] * n


for i in range(1, n):
    for j in range(i):
        if nums[i] > nums[j]:
            dp[i] = max(dp[j] + 1, dp[i])

print(max(dp))