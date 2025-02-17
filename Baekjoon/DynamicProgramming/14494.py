"""
다이나믹이 뭐에요?
문제: https://www.acmicpc.net/problem/14494
"""
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
mod = 1000000007
dp = [[1] * m for _ in range(n)]

for i in range(1, n):
    for j in range(1, m):
        dp[i][j] = (dp[i - 1][j] + dp[i][j - 1] + dp[i - 1][j - 1]) % mod

print(dp[n-1][m-1])