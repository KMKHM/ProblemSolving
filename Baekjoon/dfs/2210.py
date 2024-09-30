"""
숫자판 점프
문제: https://www.acmicpc.net/problem/2210
"""
import sys

input = sys.stdin.readline

s = set()

board = [list(input().split()) for _ in range(5)]

dx, dy = (1, -1, 0, 0), (0, 0, 1, -1)

def dfs(x, y, cnt, val):

    if cnt == 6:
        s.add(val)
        return

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < 5 and 0 <= ny < 5:
            dfs(nx, ny, cnt + 1, val + board[nx][ny])

for i in range(5):
    for j in range(5):
        dfs(i, j, 1, board[i][j])

print(len(s))