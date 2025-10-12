"""
https://www.acmicpc.net/problem/10844
"""
mod = 1_000_000_000
n = int(input())

dp = [0] * (n+1)
dp[1] = 9

for i in range(2, n+1):
    dp[i] = dp[i-1]