"""
컴백홈
문제: https://www.acmicpc.net/problem/1189
"""
import sys

input = sys.stdin.readline

r, c, k = map(int, input().split())

board = [list(input().rstrip()) for _ in range(r)]
visited = [[0]*c for _ in range(r)]

ans = 0

dx, dy = (1, -1, 0, 0), (0, 0, 1, -1)
def dfs(x, y, cnt):
    global ans

    visited[x][y] = 1

    if (x, y) == (0, c-1):
        if cnt == k:
            ans += 1
            return

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0<=nx<r and 0<=ny<c:
            if not visited[nx][ny] and board[nx][ny] == ".":
                visited[nx][ny] = 1
                dfs(nx, ny, cnt + 1)
                visited[nx][ny] = 0

dfs(r-1, 0, 1)

print(ans)