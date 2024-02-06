"""
농장 관리
문제: https://www.acmicpc.net/problem/1245
"""
import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]

visitd = [[0] * m for _ in range(n)]

dx = (1, -1, 0, 0, 1, -1, 1, -1)
dy = (0, 0, 1, -1, 1, -1, -1, 1)


def bfs(x, y):
    q = deque()
    q.append([x, y])
    visitd[x][y] = 1
    flag = True

    while q:
        cur_x, cur_y = q.popleft()

        for i in range(8):
            nx, ny = cur_x + dx[i], cur_y + dy[i]
            if 0<=nx<n and 0<=ny<m:
                if not visitd[nx][ny] and board[cur_x][cur_y] == board[nx][ny]:
                    q.append([nx, ny])
                    visitd[nx][ny] = 1
                elif board[nx][ny] > board[cur_x][cur_y]:
                    flag = False

    return True if flag else False

ans = 0

for i in range(n):
    for j in range(m):
        if not visitd[i][j] and board[i][j] != 0:
            if bfs(i, j):
                ans += 1

print(ans)
