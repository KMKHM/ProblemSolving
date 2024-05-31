"""
자원 캐기
문제: https://www.acmicpc.net/problem/14430
"""
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

dp = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(m):
        if i == 0 and j == 0:
            continue
        elif j == 0:
            dp[i][j] += dp[i-1][j]
        elif i == 0:
            dp[i][j] += dp[i][j-1]
        else:
            dp[i][j] = max(dp[i][j-1] + dp[i][j], dp[i-1][j] + dp[i][j])

print(dp[n-1][m-1])