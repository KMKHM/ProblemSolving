"""
소문난 칠공주
문제: https://www.acmicpc.net/problem/1941
"""
import sys
from collections import Counter
input = sys.stdin.readline

board = [list(input().rstrip()) for _ in range(5)]

limit = 7

cnt = 0
temp = []
dx, dy = (1, -1, 0, 0), (0, 0, 1, -1)

check = [[0]*5 for _ in range(5)]

a = set()

def backtracking(x, y, s):

    global cnt

    if s.count("Y") >= 4:
        return

    if len(temp) == 7:
        nums = tuple(sorted(temp))
        if nums not in a:
            a.add(nums)
            cnt += 1
        return

    for u, v in temp:
        for i in range(4):
            nx, ny = u + dx[i], v + dy[i]
            if 0 <= nx < 5 and 0 <= ny < 5 and (nx, ny) not in temp:
                temp.append((nx, ny))
                backtracking(nx, ny, s + board[nx][ny])
                temp.pop()


for i in range(5):
    for j in range(5):
        temp.append((i, j))
        backtracking(i, j, board[i][j])
        temp.pop()

print(len(a))