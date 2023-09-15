"""
무기 공학
문제: https://www.acmicpc.net/problem/18430
"""
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]

if n*m < 3:
    print(0)
    sys.exit(0)

# ㄱ자 방향
dx = (1, -1, 0, 0)
dy = (0, 0, 1, -1)

# 방문여부
visited = [[0]*m for _ in range(n)]

ans = 0

res = []

def backtracking(x, y, cnt):
    global ans

    if cnt == 3:
        res.append(ans)

    visited[x][y] = 1

    # 4방향
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<m:
            if not visited[nx][ny]:
                visited[nx][ny] = 1
                ans += board[nx][ny]
                backtracking(nx, ny)
                ans -= board[nx][ny]
                visited[nx][ny] = 0




