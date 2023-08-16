"""
전쟁 - 전투
문제: https://www.acmicpc.net/problem/1303
"""
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

board = [list(input().rstrip()) for _ in range(m)]

visited = [[False]*n for _ in range(m)]

dx = (1, -1, 0, 0)
dy = (0, 0, 1, -1)

white, blue = 0, 0

def dfs(x, y, type):
    visited[x][y] = True
    cnt = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
            if board[nx][ny] == type:
                visited[nx][ny] = True
                cnt += dfs(nx, ny, type)

    return cnt

for i in range(m):
    for j in range(n):
        if not visited[i][j]:
            if board[i][j] == "W":
                white += dfs(i, j, "W")**2
            else:
                blue += dfs(i, j, "B")**2

print(white, blue)