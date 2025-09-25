"""
미로 탈출
문제: https://www.acmicpc.net/problem/14923
"""
import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

hx, hy = map(int, input().split())

ex, ey = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]
visited = [[[0]*2 for _ in range(m)] for _ in range(n)]

dx, dy = (1, -1, 0, 0), (0, 0, 1, -1)

def bfs(x, y):
    q = deque()
    q.append([x, y, 0, 1])
    visited[x][y][0] = 1

    while q:
        curx, cury, cnt, magic = q.popleft()
        # print(curx, cury)
        if curx == ex-1 and cury == ey-1:
            return cnt

        for i in range(4):
            nx, ny = curx + dx[i], cury + dy[i]
            if 0<=nx<n and 0<=ny<m:
                if board[nx][ny] == 1 and not visited[nx][ny][magic] and magic == 1: # 벽인 경우
                    visited[nx][ny][magic] = 1
                    q.append([nx, ny, cnt+1, 0])
                elif board[nx][ny] == 0 and not visited[nx][ny][magic]: # 벽 아닌 경우
                    visited[nx][ny][magic] = 1
                    q.append([nx, ny, cnt+1, magic])
    return -1

print(bfs(hx-1, hy-1))
