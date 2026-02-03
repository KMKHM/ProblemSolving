"""
https://www.acmicpc.net/problem/21938
"""
import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]
board = []

t = int(input())

for i in range(n):
    ls = []
    for j in range(0, 3*m-2, 3):
        ls.append(255 if graph[i][j] + graph[i][j+1] + graph[i][j+2] >= t*3 else 0)
    board.append(ls)

check = [[0]*m for _ in range(n)]

dx, dy = (0, 0, 1, -1), (1, -1, 0, 0)

def bfs(x, y):
    check[x][y] = 1
    q = deque([(x, y)])
    while q:
        curx, cury = q.popleft()
        for i in range(4):
            nx = curx + dx[i]
            ny = cury + dy[i]
            if 0<=nx<n and 0<=ny<m and not check[nx][ny] and board[nx][ny] == 255:
                check[nx][ny] = 1
                q.append((nx, ny))

res = 0
for i in range(n):
    for j in range(m):
        if not check[i][j] and board[i][j] == 255:
            res += 1
            bfs(i, j)
print(res)