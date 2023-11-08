"""
공주님을 구해라!
문제: https://www.acmicpc.net/problem/17836
"""
import sys

from collections import deque

input = sys.stdin.readline

n, m, t = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]

visited = [[0]*m for _ in range(n)]

dx, dy = (1, -1, 0, 0), (0, 0, -1, 1)

def bfs(x, y):
    q = deque()
    q.append([x, y, 0])
    visited[x][y] = 1
    while q:
        a, b, sword = q.popleft()
        for i in range(4):
            nx, ny = a + dx[i], b + dy[i]
            if 0<=nx<n and 0<=ny<m:
                if (nx, ny) == (n-1, m-1):
                    visited[nx][ny] = min(visited[nx][ny], visited[a][b] + 1)
                if not visited[nx][ny] and sword == 1:
                    visited[nx][ny] = visited[a][b] + 1
                    q.append([nx, ny, 1])
                else:
                    if not visited[nx][ny]:
                        visited[nx][ny] = visited[a][b] + 1
                        if board[nx][ny] == 0:
                            q.append([nx, ny, 0])
                        elif board[nx][ny] == 2:
                            q.append([nx, ny, 1])
                        elif board[nx][ny] == 1:
                            continue

bfs(0,0)
for i in range(n):
    print(*visited[i])


