"""
병사 배치하기
문제: https://acmicpc.net/problem/18353
"""
import sys

input = sys.stdin.readline

n = int(input())

nums = list(map(int, input().split()))

dp = [1] * n

for i in range(1, n):
    for j in range(i):
        if nums[i] < nums[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(n - max(dp))


