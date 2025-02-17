"""
죽음의 비
문제: https://www.acmicpc.net/problem/22944
"""
import sys
from collections import deque

input = sys.stdin.readline

n, h, d = map(int, input().split())

board = [list(input().rstrip()) for _ in range(n)]

dx, dy = (1, -1, 0, 0), (0, 0, -1, 1)

s, e = [], []

for i in range(n):
    for j in range(n):
        if board[i][j] == "S":
            s = [i, j]
        if board[i][j] == "E":
            e = [i, j]

visited = [[0]*n for _ in range(n)]

def bfs(a, b):
    q = deque()
    q.append([a, b, h, 0, 0])
    visited[a][b] = h
    while q:
        x, y, now_h, now_d, m = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0<=nx<n and 0<=ny<n and visited[nx][ny] < visited[x][y]:
                if now_h <= 0 and now_d <= 0:
                    continue
                else:
                    if board[nx][ny] == "E":
                        return m + 1

                    elif board[nx][ny] == ".":
                        if now_d > 0:
                            q.append([nx, ny, now_h, now_d - 1, m + 1])
                            visited[nx][ny] = now_h
                        else:
                            q.append([nx, ny, now_h - 1, now_d, m + 1])
                            visited[nx][ny] = now_h - 1

                    elif board[nx][ny] == "U":
                        if now_d > 0:
                            q.append([nx, ny, now_h, d, m + 1])
                            visited[nx][ny] = now_h
                        else:
                            q.append([nx, ny, now_h - 1, d, m + 1])
                            visited[nx][ny] = now_h - 1
    return -1

print(bfs(s[0], s[1]))
