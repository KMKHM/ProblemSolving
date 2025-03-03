"""
침투
문제: https://www.acmicpc.net/problem/13565
"""
import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

board = [list(input().rstrip()) for _ in range(n)]

visited = [[0]*m for _ in range(n)]

dx, dy = (1, -1, 0, 0), (0, 0, 1, -1)

def bfs(x, y):
    q = deque()
    q.append([x, y])
    visited[x][y] = 1

    while q:
        cur_x, cur_y = q.popleft()
        if cur_x == n - 1:
            return True

        for i in range(4):
            nx, ny = cur_x + dx[i], cur_y + dy[i]
            if 0<=nx<n and 0<=ny<m and not visited[nx][ny] and board[nx][ny] == "0":
                visited[nx][ny] = 1
                q.append([nx, ny])
    return False

for j in range(m):
    if not visited[0][j] and board[0][j] == "0":
        if bfs(0, j):
            print("YES")
            sys.exit(0)
print("NO")
