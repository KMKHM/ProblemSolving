"""
목장 건설하기
문제: https://www.acmicpc.net/problem/14925
"""
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * (m+1) for _ in range(n+1)]

ans=0

for i in range(1, n+1):
    for j in range(1, m+1):
        if board[i-1][j-1] == 0:
            dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
            ans=max(ans, dp[i][j])

print(ans)