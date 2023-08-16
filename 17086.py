"""
아기 상어 2
https://www.acmicpc.net/problem/17086
"""

import sys

input = sys.stdin.readline

n, m = map(int, input().split())

board = []

for _ in range(n):
    board.append(list(map(int, input().split())))


visied = [[0]*m for _ in range(n)]

answer = 0

dx = [-1, -1, 0, 1, 1, 0, -1, 1]
dy = [0, 1, 1, 1, -1, -1, -1, 0]


def dfs(x, y):
    global answer

    visied[x][y] = 1

    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<m:
            pass

