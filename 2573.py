"""
빙산
문제: https://www.acmicpc.net/problem/2573
"""
import sys
from copy import deepcopy
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]


def melting():
    copy_arr = [[0]*m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if board[i][j]:
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0<=nx<n and 0<=ny<m:
                        if board[nx][ny] == 0:
                            copy_arr[i][j] -= 1

    for i in range(n):
        for j in range(m):
            if board[i][j] + copy_arr[i][j] < 0:
                board[i][j] = 0
            else:
                board[i][j] += copy_arr[i][j]




def bfs(x, y, cnt, visited):
    q = deque()
    q.append([x, y])
    visited[x][y] = 1
    while q:
        now_x, now_y = q.popleft()
        for i in range(4):
            nx = now_x + dx[i]
            ny = now_y + dy[i]
            if 0<=nx<n and 0<=ny<m and not visited[nx][ny] and board[nx][ny]!=0:
                cnt += 1
                visited[nx][ny] = 1
                q.append([nx, ny])
    return cnt

answer = 0

while 1:
    tmp = 0
    for i in range(n):
        tmp += sum(board[i])
    if tmp == 0:
        print(0)
        exit(0)

    visited = [[0] * m for _ in range(n)]

    tmp_answer = 0

    for i in range(n):
        for j in range(m):
            if not visited[i][j] and board[i][j] != 0:
                if bfs(i, j, 1, visited):
                    tmp_answer += 1

    if tmp_answer < 2:
        melting()
        answer += 1
        continue
    else:
        break


print(answer)