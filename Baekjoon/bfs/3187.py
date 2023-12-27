"""
양치기 꿍
문제: https://www.acmicpc.net/problem/3187
"""
import sys
from collections import deque

input = sys.stdin.readline

r, c = map(int, input().split())

board = [list(input().rstrip()) for _ in range(r)]

dx, dy = (1, -1, 0, 0), (0, 0, 1, -1)

visited = [[0]*c for _ in range(r)]

ans = [0, 0]

def bfs(x, y):
    q = deque()
    q.append([x, y])
    visited[x][y] = 1
    goat, wolf = 0, 0
    if board[x][y] == "k":
        goat += 1
    elif board[x][y] == "v":
        wolf += 1

    while q:
        cx, cy = q.popleft()
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0<=nx<r and 0<=ny<c and not visited[nx][ny] and board[nx][ny] != "#":
                visited[nx][ny] = 1
                q.append([nx, ny])
                if board[nx][ny] == "k":
                    goat += 1
                if board[nx][ny] == "v":
                    wolf += 1
    if goat > wolf:
        ans[0] += goat
    else:
        ans[1] += wolf

for i in range(r):
    for j in range(c):
        if not visited[i][j] and board[i][j] != "#":
            bfs(i, j)

print(*ans)