"""
내리막길
문제: https://www.acmicpc.net/problem/1520
"""
import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

n, m = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# 정답
answer = 0

def dfs(x, y):
    global answer

    if x == n-1 and y == m-1:
        answer += 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<m:
            if board[x][y] > board[nx][ny]:
                dfs(nx, ny)

dfs(0, 0)

print(answer)