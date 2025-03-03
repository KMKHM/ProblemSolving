"""
말이 되고픈 원숭이
문제: https://www.acmicpc.net/problem/1600
"""
import sys
from collections import deque

input = sys.stdin.readline

k = int(input())

w, h = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(h)]

dx, dy = (1, -1, 0, 0), (0, 0, 1, -1)
hx, hy = (-2, -1, -2, -1, 1, 2, 1, 2), (-1, -2, 1, 2, -2, -1, 2, 1)
check = [[0]*w for _ in range(h)]
def bfs(x, y):
    q = deque()
    q.append([x, y, k, 0])
    check[x][y] = 1

    while q:
        curx, cury, curk, cnt = q.popleft()
        if curx == h-1 and cury == w-1:
            return cnt
        for i in range(4):
            nx, ny = curx + dx[i], cury + dy[i]
            if 0 <= nx < h and 0 <= ny < w and not check[nx][ny] and board[nx][ny] == 0:
                check[nx][ny] = 1
                q.append([nx, ny, curk, cnt + 1])
        if curk > 0:
            for i in range(8):
                nx2, ny2 = curx + hx[i], cury + hy[i]
                if 0 <= nx2 < h and 0 <= ny2 < w and not check[nx2][ny2] and board[nx2][ny2] == 0:
                    check[nx2][ny2] = 1
                    q.append([nx2, ny2, curk - 1, cnt + 1])

    return -1

print(bfs(0, 0))