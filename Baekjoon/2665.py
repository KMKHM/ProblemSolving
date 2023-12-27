"""
미로만들기
문제: https://www.acmicpc.net/problem/2665
"""
import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

board = [list(input().rstrip()) for _ in range(n)]

visited = [[0] * n for _ in range(n)]

dx, dy = (1, 0), (0, 1)

def cal_distance(r1, c1, r2, c2):
    return abs(r1-r2) + abs(c1-c2)

def bfs(sx, sy):
    q = deque()
    q.append([sx, sy])
    visited[sx][sy] = 1
    cnt = 0

    while q:
        cx, cy = q.popleft()
        if (cx, cy) == (n-1, n-1):
            return cnt
        for i in range(2):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if board[nx][ny] == "1":
                    visited[nx][ny] = 1
                    q.append([nx, ny])
                elif board[nx][ny] == "0":
                    if (ny +1 < n and board[nx][ny+1] == "1") or (nx + 1 < n and board[nx+1][ny] == "1"):
                        cnt += 1
                        print(nx, ny)
                        visited[nx][ny] = 1
                        q.append([nx, ny])
    return 0

print(bfs(0, 0))