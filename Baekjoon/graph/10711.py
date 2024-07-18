"""
모래성
문제: https://www.acmicpc.net/problem/10711
"""
import sys
from collections import deque

input = sys.stdin.readline

h, w = map(int, input().split())

board = []
nums = deque()

for i in range(h):
    board.append(list(input().rstrip()))
    for j in range(w):
        if board[i][j].isdigit():
            board[i][j] = int(board[i][j])
        else:
            board[i][j] = 0
            nums.append([i, j])

dx = (1, -1, 0, 0, 1, -1, 1, -1)
dy = (0, 0, 1, -1, 1, -1, -1, 1)

wave = 0

check = [[0] * w for _ in range(h)]

while nums:
    cur_x, cur_y = nums.popleft()
    for i in range(8):
        nx, ny = cur_x + dx[i], cur_y + dy[i]
        if 0<=nx<h and 0<=ny<w:
            if board[nx][ny]:
                board[nx][ny] -= 1
                if not board[nx][ny]:
                    nums.append([nx, ny])
                    check[nx][ny] = check[cur_x][cur_y] + 1
                    wave = max(wave, check[nx][ny])
print(wave)