"""
드래곤 커브
문제: https://www.acmicpc.net/problem/15685
"""
import sys

input = sys.stdin.readline

direction = {0: [1, 0], 1: [0, -1], 2: [-1, 0], 3: [1, 0]}

n = int(input())

curve = [list(map(int, input().split())) for _ in range(3)]

board = [[0]*101 for _ in range(101)]

for i in range(n):
    # 시작 좌표, 시작 방향, 세대
    x, y, d, g = curve[i]

    if not(0 <= x <= 100 and 0 <= y <= 100):
        continue

    board[x][y] = 1

    for _ in range(g):
        dx, dy = x + direction[d][0], y + direction[d][1]
        if 0 <= dx <= 100 and 0 <= dy <= 100:
            board[dx][dy] = 1
        if d == 0:
            d = 3
        elif d == 3:
            d = 2
        elif d == 2:
            d = 1
        else:
            d = 0


