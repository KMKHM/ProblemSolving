"""
가장 긴 증가하는 부분 수열 5
문제: https://www.acmicpc.net/problem/14003
"""
import sys

input = sys.stdin.readline

n = int(input())

nums = list(map(int, input().split()))

dp = [[i] for i in nums]

for i in range(1, n):
    for j in range(i):
        if nums[i] > nums[j] and len(dp[j]) + 1 > len(dp[i]):
            dp[i] = dp[j] + [nums[i]]

ans = max(dp, key=len)

print(len(ans))
print(*ans)