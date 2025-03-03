"""
보물섬
문제: https://www.acmicpc.net/problem/2589
"""
import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

board = [list(input().rstrip()) for _ in range(n)]

dx, dy = (1, -1, 0, 0), (0, 0, 1, -1)
def bfs(x, y):
    visited = [[0] * m for _ in range(n)]
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    cnt = 0

    while q:
        now_x, now_y = q.popleft()
        for i in range(4):
            nx, ny = now_x + dx[i], now_y + dy[i]
            if 0<=nx<n and 0<=ny<m and board[nx][ny] == "L" and not visited[nx][ny]:
                visited[nx][ny] = visited[now_x][now_y] + 1
                cnt = max(visited[nx][ny], cnt)
                q.append((nx, ny))
    return cnt - 1


answer = 0


for i in range(n):
    for j in range(m):
        if board[i][j] == "L":
            answer = max(answer, bfs(i, j))


print(answer)
