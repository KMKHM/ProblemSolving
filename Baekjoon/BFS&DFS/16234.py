"""
인구이동
문제: https://www.acmicpc.net/problem/16234
"""
import sys
from collections import deque

input = sys.stdin.readline

n, l, r = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    q = deque()
    union = []
    q.append((x, y))
    union.append((x, y))
    while q:
        now_x, now_y = q.popleft()
        for k in range(4):
            nx = now_x + dx[k]
            ny = now_y + dy[k]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
                if l<=abs(board[nx][ny] - board[now_x][now_y])<=r:
                    visited[nx][ny] = 1
                    union.append((nx, ny))
                    q.append((nx, ny))

    return union

# 정답
answer = 0

while True:
    flag = 0
    visited = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                visited[i][j] = 1
                country = bfs(i, j)

                if len(country) > 1:
                    flag = 1
                    people = sum(board[x][y] for x, y in country) // len(country)

                    for x, y in country:
                        board[x][y] = people
    if flag == 0:
        print(answer)
        break
    answer+=1