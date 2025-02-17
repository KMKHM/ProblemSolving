"""
점프
문제: https://www.acmicpc.net/problem/1890
"""
import sys

input = sys.stdin.readline

n = int(input())

board = [list(map(int, input().split())) for _ in range(n)]

# DynamicProgramming 테이블
dp = [[0]*n for _ in range(n)]

# 시작지점
start = board[0][0]

# 시작지점에서 갈 수 있는 곳 1가지로 초기화
dp[start][0] = dp[0][start] = 1

for i in range(n):
    for j in range(n):
        if dp[i][j] and (i, j) != (n-1, n-1):
            nx, ny = i + board[i][j], j + board[i][j]

            if nx < n:
                dp[nx][j] += dp[i][j]
            if ny < n:
                dp[i][ny] += dp[i][j]

print(dp[-1][-1])