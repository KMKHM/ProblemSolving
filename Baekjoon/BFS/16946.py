"""
벽 부수고 이동하기 4
문제: https://www.acmicpc.net/problem/16946
"""
import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

board = [list(map(int, list(input().rstrip()))) for _ in range(n)]
ans = [[0]*m for _ in range(n)]
dx, dy = (1, -1, 0, 0), (0, 0, 1, -1)
visited = [[0]*m for _ in range(n)]
v=1
def bfs(x, y):
    q = deque()
    q.append([x, y])
    check=[[x, y]]
    visited[x][y]=v
    cnt=1

    while q:
        cur_x, cur_y = q.popleft()
        for i in range(4):
            nx, ny = cur_x + dx[i], cur_y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and board[nx][ny] == 0:
                q.append([nx, ny])
                check.append([nx, ny])
                visited[nx][ny]=v
                cnt+=1
    for a, b in check:
        ans[a][b] = cnt

for i in range(n):
    for j in range(m):
        if board[i][j] == 0 and not visited[i][j]:
            bfs(i, j)
            v+=1

for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            w = 1
            tmp=[]
            for k in range(4):
                ni, nj = i + dx[k], j + dy[k]
                if 0 <= ni < n and 0 <= nj < m and visited[ni][nj] not in tmp:
                    w+=ans[ni][nj]
                    tmp.append(visited[ni][nj])
            print(w%10, end="")
        else:
            print(0, end="")
    print()