"""
창고 다각형
문제: https://www.acmicpc.net/problem/2304
"""
import sys

input = sys.stdin.readline

n = int(input())

board = [list(map(int, input().split())) for _ in range(n)]

board.sort()

max_val = max(j for i, j in board)

res = 0

cur_x, cur_y = 0, 0

for i in range(n):
    if i == 0:
        cur_x, cur_y = board[i][0], board[i][1]

    elif i == n - 1:
        if cur_y > board[i][1]:
            res += cur_x * cur_y
        elif cur_y < board[i][1]:
            res += cur_x * cur_y - board[i][1]

    else:
        if cur_y < board[i][1]:
            res += (board[i][0] - cur_x) * cur_y
            cur_x = board[i][0]
            cur_y = board[i][1]

print(res)