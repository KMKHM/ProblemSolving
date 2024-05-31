"""
적록색약
문제: https://www.acmicpc.net/problem/10026
"""
import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

board = [list(input()) for _ in range(n)]

ans1, ans2 = {}, {}

dx, dy = (1, -1, 0, 0), (0, 0, 1, -1)
def bfs1(x, y, visited):
    q = deque()
    q.append([x, y, 1])
    visited[x][y] = 1

    while q:
        cx, cy = q.popleft()
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if not visited[nx][ny] and board[cx][cy] == board[nx][ny]:
                visited[nx][ny] = 1
                q.append([nx, ny])

for i in range(n):
    for j in range(n):



