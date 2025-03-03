"""
나이트의 이동
문제: https://www.acmicpc.net/problem/7562
"""
import sys
from collections import deque

input = sys.stdin.readline

dx, dy = (-1, -2, -2, -1, 1, 2, 2, 1), (-2, -1, 1, 2, -2, -1, 1, 2)

def bfs(n, check, start_x, start_y, end_x, end_y):
    q = deque()
    q.append([start_x, start_y])

    while q:
        cur_x, cur_y = q.popleft()

        if cur_x == end_x and cur_y == end_y:
            return check[cur_x][cur_y]

        for i in range(len(dx)):
            nx, ny = cur_x + dx[i], cur_y + dy[i]
            if 0<=nx<n and 0<=ny<n:
                if not check[nx][ny]:
                    check[nx][ny] = check[cur_x][cur_y] + 1
                    q.append([nx, ny])

t = int(input())

for _ in range(t):
    n = int(input())
    start_x, start_y = map(int, input().split())
    end_x, end_y = map(int, input().split())

    check = [[0]*n for _ in range(n)]

    print(bfs(n, check, start_x, start_y, end_x, end_y))