"""
1, 2, 3 더하기 4
문제: https://www.acmicpc.net/problem/15989
"""
import sys

input = sys.stdin.readline

n = int(input())

dp = [1] * 10001

for i in range(2, 10001):
    dp[i] += dp[i-2]

for i in range(3, 10001):
    dp[i] += dp[i-3]

for _ in range(n):
    print(dp[int(input())])
