"""
곡예 비행
문제: https://www.acmicpc.net/problem/21923
"""
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

dp = [list(map(int, input().split())) for _ in range(n)]

# 상승
for i in range(n-1, -1, -1):
    for j in range(m):
        print(i, j)
        if i == n-1 and j == 0:
            continue
        elif i == n - 1:
            dp[i][j] += dp[i][j-1]
        elif j == 0:
            dp[i][j] += dp[i-1][j]
        else:
            dp[i][j] = max(dp[i][j] + dp[i-1][j], dp[i][j] + dp[i][j-1])
for d in dp:
    print(*d)