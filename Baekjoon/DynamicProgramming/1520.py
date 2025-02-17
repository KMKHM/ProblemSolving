"""
내리막 길
문제: https://www.acmicpc.net/problem/1520
"""
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * m for _ in range(n)]


dx = (1, -1, 0, 0)
dy = (0, 0, 1, -1)

ans = 0

for i in range(n):
    for j in range(m):
        cnt = 0
        for k in range(4):
            nx = i + dx[k]
            ny = i + dy[k]
            if 0<=nx<n and 0<=ny<m:
                if board[i][j] <= board[nx][ny]:
                    cnt += 1
        if cnt == 0:
            continue

        dp[i][j] = cnt

print(dp[-1][-1])
