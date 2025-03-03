"""
경쟁적 전염
문제: https://www.acmicpc.net/problem/18405
"""
import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]

s, x, y = map(int, input().split())

dx, dy = (1, -1, 0, 0), (0, 0, 1, -1)

visited = [[0]*n for _ in range(n)]

def bfs(num):
    q = deque()
    for i in range(n):
        for j in range(n):
            if board[i][j] == num and not visited[i][j]:
                q.append((i, j))

    while q:
        now_x, now_y = q.popleft()
        for i in range(4):
            nx, ny = now_x + dx[i], now_y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not board[nx][ny]:
                visited[i][j] = 1
                board[nx][ny] = board[now_x][now_y]


for _ in range(s):
    for num in range(1, k+1):
        bfs(num)


print(board[x-1][y-1])



