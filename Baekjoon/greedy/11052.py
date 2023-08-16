"""
카드 구매하기
문제: https://www.acmicpc.net/problem/11052
"""
import sys

input = sys.stdin.readline

n = int(input())

nums = [0] + list(map(int, input().split()))

dp = [0] * (n+1)

dp[1] = nums[1]

for i in range(2, n+1):
    for j in range(1, i):
        if i % j == 0:
            dp[i] = max(nums[i], dp[j] * (i//j), dp[i])
        else:
            dp[i] = max(nums[i], dp[i-j] + dp[j], dp[i])



print(dp[-1])

