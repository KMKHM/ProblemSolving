"""
다리 만들기
문제: https://www.acmicpc.net/problem/2146
"""
import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

board = [list(map(int, input().split())) for _ in range(n)]

visited = [[0]*n for _ in range(n)]

dx, dy = (0, 0, 1, -1), (1, -1, 0, 0)

def bfs(x, y):
    q = deque()
    q.append([x, y])
    visited[x][y] = 1
    edge = set()
    while q:
        cur_x, cur_y = q.popleft()
        for i in range(4):
            nx, ny = cur_x + dx[i], cur_y + dy[i]
            if 0<= nx < n and 0<= ny < n:
                if not visited[nx][ny] and board[nx][ny] == 1:
                    visited[nx][ny] = 1
                    q.append([nx, ny])
                if board[nx][ny] == 0:
                    edge.add((cur_x, cur_y))
    return edge
cnt = 2

for i in range(n):
    for j in range(n):
        if not visited[i][j] and board[i][j] == 1:
            for x, y in bfs(i, j):
                visited[x][y] = cnt
            cnt += 1

def bfs2(x, y):
    q = deque()
    q.append([x, y, 0])
    check = [[0]*n for _ in range(n)]
    check[x][y] = 1
    while q:
        cur_x, cur_y, cur_cnt = q.popleft()
        if visited[cur_x][cur_y] not in [0, 1] and visited[cur_x][cur_y] != visited[x][y]:
            return cur_cnt-1
        for i in range(4):
            nx, ny = cur_x + dx[i], cur_y + dy[i]
            if 0<= nx < n and 0<= ny < n:
                if visited[nx][ny] == 1:
                    continue
                if not check[nx][ny] and visited[nx][ny] != visited[x][y]:
                    check[nx][ny] = 1
                    q.append([nx, ny, cur_cnt+1])
    return 100

ans = sys.maxsize

for i in range(n):
    for j in range(n):
        if visited[i][j] not in [0, 1]:
            a = bfs2(i, j)
            ans = min(ans, a)
print(ans)
