"""
진우의 민트초코우유
문제: https://www.acmicpc.net/problem/20208
"""
import sys

input = sys.stdin.readline

n, m, h = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]

visited = [[0]*n for _ in range(n)]

dx, dy = (1, -1, 0, 0), (0, 0, 1, -1)

start = [0, 0]

for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            start[0], start[1] = i, j
            break

answer = 0

def dfs(x, y, a, cnt):
    global answer

    if a == 0:
        return

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0<=nx<n and 0<=ny<n:
            if not visited[nx][ny]:
                if board[nx][ny] == 2:
                    visited[nx][ny] = 1
                    board[nx][ny] = 0
                    dfs(nx, ny, a -1 + h, cnt + 1)
                    visited[nx][ny] = 0
                elif board[nx][ny] == 0:
                    visited[nx][ny] = 1
                    dfs(nx, ny, a - 1, cnt)
                    visited[nx][ny] = 0
                else:
                    answer = max(answer, cnt)
                    return

dfs(start[0], start[1], m, 0)

print(answer)