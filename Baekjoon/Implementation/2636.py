"""
치즈
문제: https://www.acmicpc.net/problem/2636
"""
import sys
from copy import deepcopy
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

cheese = [list(map(int, input().split())) for _ in range(n)]

dx = (1, -1, 0, 0)
dy = (0, 0, 1, -1)

def melting(cnt):
    visited = [[0]*m for _ in range(n)]
    q = deque([(0, 0)])
    visited[0][0] = 1

    while q:
        now_x, now_y = q.popleft()
        for i in range(4):
            nx, ny = now_x + dx[i], now_y + dy[i]
            if 0<=nx<n and 0<=ny<m and not visited[nx][ny]:
                if cheese[nx][ny] == 0:
                    visited[nx][ny] = 1
                    q.append((nx, ny))
                elif cheese[nx][ny] == 1:
                    visited[nx][ny] = 1
                    cheese[nx][ny] = 0
                    cnt += 1

    return cnt

t = 0
ans = []
while 1:

    ans.append(melting(0))
    t += 1
    if ans[-1] == 0:
        break

print(t-1)
print(ans[-2])






