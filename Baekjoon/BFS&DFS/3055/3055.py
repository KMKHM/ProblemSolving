import sys
from collections import deque

input = sys.stdin.readline

r, c = map(int, input().split())
board = [list(input().strip()) for _ in range(r)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

water_time = [[-1]*c for _ in range(r)]
hedgehog_time = [[-1]*c for _ in range(r)]

water_q = deque()
hedgehog_q = deque()

# 위치 초기화
for i in range(r):
    for j in range(c):
        if board[i][j] == '*':
            water_q.append((i, j))
            water_time[i][j] = 0
        elif board[i][j] == 'S':
            hedgehog_q.append((i, j))
            hedgehog_time[i][j] = 0
        elif board[i][j] == 'D':
            dest = (i, j)

# 물 BFS 먼저
while water_q:
    x, y = water_q.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < r and 0 <= ny < c:
            if board[nx][ny] == '.' and water_time[nx][ny] == -1:
                water_time[nx][ny] = water_time[x][y] + 1
                water_q.append((nx, ny))

# 고슴도치 BFS
while hedgehog_q:
    x, y = hedgehog_q.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < r and 0 <= ny < c:
            if (board[nx][ny] == '.' or board[nx][ny] == 'D') and hedgehog_time[nx][ny] == -1:
                # 물보다 먼저 도착해야 함
                next_time = hedgehog_time[x][y] + 1
                if water_time[nx][ny] == -1 or next_time < water_time[nx][ny]:
                    hedgehog_time[nx][ny] = next_time
                    hedgehog_q.append((nx, ny))

ex, ey = dest
if hedgehog_time[ex][ey] == -1:
    print("KAKTUS")
else:
    print(hedgehog_time[ex][ey])