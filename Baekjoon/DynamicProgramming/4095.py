"""
최대 정사각형
문제: https://www.acmicpc.net/problem/4095
"""
import sys

input = sys.stdin.readline

while True:
    n, m = map(int, input().split())

    if n == 0 and m == 0:
        sys.exit(0)

    dp = [[0] * (m+1) for _ in range(n+1)]

    board = [list(map(int, input().split())) for _ in range(n)]

    val = 0

    for i in range(1, n+1):
        for j in range(1, m+1):
            if board[i-1][j-1] == 1:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                val = max(val, dp[i][j])
    print(val)