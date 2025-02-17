"""
Game Addiction
문제: https://www.acmicpc.net/problem/20152
"""
import sys

h, n = map(int, input().split())

h, n = min(h, n), max(h, n)

dp = [[sys.maxsize]*(n+1) for _ in range(n+1)]

dp[h][h] = 1

for i in range(h, n+1):
    for j in range(h, n+1):
        if i < j:
            continue
        if i == 0:
            dp[i][j] = min(dp[i][j], dp[i-1][j] + 1)
        