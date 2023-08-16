"""
연구소 2
문제: https://www.acmicpc.net/problem/17141
"""
import sys
from itertools import combinations
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]

virus = []

for i in range(n):
    for j in range(n):
        if board[i][j] == 2:
            virus.append((i, j))
        if board[i][j] == 1:
            board[i][j] = -1

possible = []

for a in combinations(virus, m):
    possible.append(list(a))

dx = (1, -1, 0, 0)
dy = (0, 0, 1, -1)

def bfs(location, matrix, visited):
    q = deque()
    for x, y in location:
        matrix[x][y] = 0
        visited[x][y] = True
        q.append((x, y, 0))

    while q:
        now_x, now_y, now_time = q.popleft()
        for i in range(4):
            nx = now_x + dx[i]
            ny = now_y + dy[i]
            if 0<=nx<n and 0<=ny<n and matrix[nx][ny] != -1:
                if not visited[nx][ny]:
                    visited[nx][ny] = True
                    matrix[nx][ny] = now_time + 1
                    q.append((nx, ny, matrix[nx][ny]))

    max_time = 0
    for i in range(n):
        for j in range(n):
            if matrix[i][j] != -1 and not visited[i][j]:
                return -1

            max_time = max(max_time, matrix[i][j])

    return max_time

a1, a2 = sys.maxsize, -1
for l in possible:
    t = bfs(l, board, [[False]*n for _ in range(n)])
    if t != -1:
        a1 = min(t, a1)

print(a1 if a1 != sys.maxsize else a2)


