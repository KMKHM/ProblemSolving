"""
파도반 수열
문제: https://www.acmicpc.net/problem/9461
"""
import sys

input = sys.stdin.readline

t = int(input())

dp = [0] * 101
dp[1] = dp[2] = dp[3] = 1

for i in range(4, 101):
    dp[i] = dp[i-2] + dp[i-3]

for _ in range(t):
    print(dp[int(input())])