"""
탈출
문제: https://www.acmicpc.net/problem/3055
"""
import sys
from collections import deque

input = sys.stdin.readline

r, c = map(int, input().split())

board = [list(input().rstrip()) for _ in range(r)]

sx, sy = 0, 0
ex, ey = 0, 0

dx, dy = (0, 0, 1, -1), (1, -1, 0, 0)

check = [[0]*c for _ in range(r)]

water = deque()

for i in range(r):
    for j in range(c):
        if board[i][j] == 'S':
            sx, sy = i, j
        elif board[i][j] == 'D':
            ex, ey = i, j
        elif board[i][j] == 'X':
            check[i][j] = 1
        elif board[i][j] == "*":
            check[i][j] = 1
            water.append([i, j])

def bfs(x, y):
    q = deque()
    q.append([x, y, 0])
    check[x][y]=1

    while q:
        curx, cury, cnt = q.popleft()

        if curx == ex and cury == ey:
            return cnt

        tmp = len(water)

        for _ in range(tmp):
            a, b = water.popleft()
            for i in range(4):
                qx, qy = a + dx[i], b + dy[i]
                if 0 <= qx < r and 0 <= qy < c and not check[qx][qy] and board[qx][qy]==".":
                    water.append([qx, qy])
                    check[qx][qy]=1
                    board[qx][qy]="*"

        for i in range(4):
            nx, ny = curx + dx[i], cury + dy[i]
            if 0<=nx<r and 0<=ny<c and not check[nx][ny] and (board[nx][ny]=='.' or board[nx][ny]=='D'):
                check[nx][ny] = 1
                q.append([nx, ny, cnt+1])

    return "KAKTUS"

print(bfs(sx, sy))