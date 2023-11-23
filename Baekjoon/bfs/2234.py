"""
성곽
문제: https://www.acmicpc.net/problem/2234
"""
import sys
from collections import deque

input = sys.stdin.readline

m, n = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]

# 이진수 변환
for i in range(n):
    for j in range(m):
        board[i][j] = bin(board[i][j])[2:].zfill(4)


# 1번째가 0이면 아래로갈 수 있음
# 2번재가 0이면 오른쪽으로 갈 수 있음
# 3번째가 0이면 위쪽으로 갈 수 있음
# 4번째가 0이면 왼쪽으로갈 수 있음

visited = [[0] * m for _ in range(n)]

def check(x, y):
    go = []
    tmp = board[x][y]
    if tmp[0] == "0": # 아래
        go.append((1, 0))
    if tmp[1] == "0": # 오른쪽
        go.append((0, 1))
    if tmp[2] == "0": # 위쪽
        go.append((-1, 0))
    if tmp[3] == "0": # 왼쪽
        go.append((0, -1))
    return go

def bfs(x, y, num):
    q = deque()
    q.append([x, y])
    cnt = 1
    while q:
        now_x, now_y = q.popleft()
        for dx, dy in check(now_x, now_y):
            nx, ny = now_x + dx, now_y + dy
            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny]:
                    visited[nx][ny] = num
                    cnt += 1
                    q.append([nx, ny])
    return cnt

total_area = 0 # 전체 영역수
max_area = -1 # 가장 큰 영역
num = 1

dic = dict()

for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            visited[i][j] = num
            total_area += 1
            val = bfs(i, j, num)
            max_area = max(max_area, val)
            dic[num] = val
            num += 1

print(total_area)
print(max_area)


d1, d2 = (1, -1, 0, 0), (0, 0, 1, -1)

ans = 0

# 근접한 경우의 수
for i in range(n):
    for j in range(m):
        for k in range(4):
            ni, nj = i + d1[k], j + d2[k]
            if 0 <= ni < n and 0 <= nj < m:
                if visited[i][j] != visited[ni][nj]:
                    ans = max(ans, dic[visited[i][j]] + dic[visited[ni][nj]])

print(ans)