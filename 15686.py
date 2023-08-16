import sys

input = sys.stdin.readline

n , m = map(int, input().split())

board = []

for _ in range(n):
    board.append(list(map(int, input().split())))

visited = [[0]*n for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def dfs(x, y):
    visited[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<n and visited[nx][ny] == 0:
            dfs(nx, ny)