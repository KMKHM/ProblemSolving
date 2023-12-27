"""
양 한마리... 양 두마리...
문제: https://www.acmicpc.net/problem/11123
"""
import sys
from collections import deque

input = sys.stdin.readline

t = int(input())

dx, dy = (1, -1, 0, 0), (0, 0, 1, -1)

def bfs(x, y):
    q = deque()
    q.append([x, y])

    while q:
        cx, cy = q.popleft()
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0<=nx<h and 0<=ny<w and not visited[nx][ny] and board[nx][ny] == "#":
                visited[nx][ny] = 1
                q.append([nx, ny])



for _ in range(t):
    h, w = map(int, input().split())

    board = [list(input().rstrip()) for _ in range(h)]

    visited = [[0]*w for _ in range(h)]

    cnt = 0

    for i in range(h):
        for j in range(w):
            if not visited[i][j] and board[i][j] == "#":
                visited[i][j] = 1
                bfs(i, j)
                cnt += 1
    print(cnt)