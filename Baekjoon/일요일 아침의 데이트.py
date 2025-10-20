"""
https://www.acmicpc.net/problem/1445
"""
import sys
from collections import deque, defaultdict

input = sys.stdin.readline

n, m = map(int, input().split())

board = [list(input().rstrip()) for _ in range(n)]

sx=sy=ex=ey=0

dx, dy = (1, -1, 0, 0), (0, 0, 1, -1)

check = defaultdict(tuple)

for i in range(n):
    for j in range(m):
        check[(i, j)] = (1e9, 1e9)
        if board[i][j] == 'S':
            sx, sy = i, j
        if board[i][j] == 'F':
            ex, ey = i, j
        if board[i][j] == 'g':
            for k in range(4):
                nx, ny = i + dx[k], j + dy[k]
                if 0 <= nx < n and 0 <= ny < m and board[nx][ny] not in ['S', 'F', 'g']:
                    board[nx][ny] = 'a'


def bfs(sx, sy, ex, ey):

    q = deque()
    q.append((sx, sy, 0, 0))
    check[(sx, sy)] = (0, 0) # 쓰레기 수, 인접쓰레기 수

    while q:
        curx, cury, curg, curag = q.popleft()

        for i in range(4):
            nx, ny = curx + dx[i], cury + dy[i]
            temp_g, temp_ag = curg, curag
            if 0<=nx<n and 0<=ny<m:
                if board[nx][ny] == 'g':
                    temp_g += 1
                if board[nx][ny] == 'a':
                    temp_ag += 1
                # 현재가 더 작을때만 넣어줌
                if check[(nx, ny)] > (temp_g, temp_ag):
                    check[(nx, ny)] = (temp_g, temp_ag)
                    q.append((nx, ny, temp_g, temp_ag))

    return check[(ex, ey)]

print(*bfs(sx, sy, ex, ey))