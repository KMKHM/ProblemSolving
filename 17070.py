"""
파이프 옮기기 1
문제: https://www.acmicpc.net/problem/17070
"""

import sys

input = sys.stdin.readline

n = int(input())

board = []

for _ in range(n):
    board.append(list(map(int, input().split())))

# 정답
answer = 0

# 매개변수로 좌표(x,y)와 방향(가로, 세로, 대각선)을 넣는다.
def dfs(x, y, dir):
    global answer

    if x == n-1 and y == n-1:
        answer += 1
        return

    if dir == 0 or dir == 2:
        if y+1 < n:
            if board[x][y+1] == 0:
                dfs(x, y+1, 0)

    if dir == 1 or dir == 2:
        if x+1 < n:
            if board[x+1][y] == 0:
                dfs(x+1, y, 1)

    if dir == 0 or dir == 1 or dir == 2:
        if x+1 < n and y+1 < n:
            if board[x+1][y] == 0 and board[x][y+1] == 0 and board[x+1][y+1] == 0:
                dfs(x+1, y+1, 2)

dfs(0, 1, 0)

print(answer)