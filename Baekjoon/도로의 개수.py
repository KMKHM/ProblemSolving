"""
https://www.acmicpc.net/problem/1577
"""
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
k = int(input())

blocked = set()

for _ in range(k):
    a, b, c, d = map(int, input().split())
    if (a, b) > (c, d):
        a, b, c, d = c, d, a, b
    blocked.add((a, b, c, d))

dp = [[0] * (m + 1) for _ in range(n + 1)]
dp[0][0] = 1

for i in range(n + 1):
    for j in range(m + 1):
        if i == 0 and j == 0:
            continue
        ways = 0
        if i > 0 and ((i-1, j, i, j) not in blocked):
            ways += dp[i-1][j]
        if j > 0 and ((i, j-1, i, j) not in blocked):
            ways += dp[i][j-1]
        dp[i][j] = ways

print(dp[n][m])