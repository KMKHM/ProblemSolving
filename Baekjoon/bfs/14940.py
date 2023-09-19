"""
쉬운 최단거리
문제: https://www.acmicpc.net/problem/14940
"""
import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]

visited = [[0]*m for _ in range(n)]

dx, dy = (1, -1, 0, 0), (0, 0, 1, -1)
def bfs(x, y):
    q = deque()
    q.append((x, y, board[x][y]))
    visited[x][y] = 1
    while q:
        cx, cy, cp = q.popleft()
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0<=nx<n and 0<=ny<m and not visited[nx][ny] and board[nx][ny] != 0:
                visited[nx][ny] = 1
                board[nx][ny] = cp + 1
                q.append((nx, ny, board[nx][ny]))

s = [0, 0]

for i in range(n):
    for j in range(m):
        if board[i][j] == 2:
            s[0], s[1] = i, j
            break

for i in range(n):
    for j in range(m):
        if board[i][j] == 1 and not visited[i][j]:
            board[i][j] = -1

board[s[0]][s[1]] = 0
bfs(s[0], s[1])


for a in board:
    print(*a)