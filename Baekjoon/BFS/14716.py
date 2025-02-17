"""
현수먁
문제: https://www.acmicpc.net/problem/14716
"""
import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]

dx, dy = (1, -1, 0, 0, 1, -1, -1, 1), (0, 0, 1, -1, 1, -1, 1, -1)

def bfs(x, y):
    q = deque()
    q.append([x, y])
    visited[x][y] = 1

    while q:
        cur_x, cur_y = q.popleft()
        for i in range(8):
            nx, ny = cur_x + dx[i], cur_y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and board[nx][ny] == 1:
                visited[nx][ny] = 1
                q.append([nx, ny])

cnt = 0

for i in range(n):
    for j in range(m):
        if not visited[i][j] and board[i][j] == 1:
            bfs(i, j)
            cnt += 1

print(cnt)