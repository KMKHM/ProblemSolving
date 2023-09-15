"""
지뢰 찾기
문제: https://www.acmicpc.net/problem/4396
"""
import sys

input = sys.stdin.readline

n = int(input())

# 지뢰
mine = [list(input().rstrip()) for _ in range(n)]

# 보드판
board = [list(input().rstrip()) for _ in range(n)]

# 8방향
dx = (1, -1, 0, 0, 1, -1, -1, 1)
dy = (0, 0, 1, -1, 1, -1, 1, -1)

# 주변에 지뢰가 몇 개 있는지 확인
def check(x, y):
    cnt = 0
    for i in range(8):
        nx, ny = x + dx[i], y + dy[i]
        if 0<=nx<n and 0<=ny<n:
            if mine[nx][ny] == "*":
                cnt += 1
    return cnt

# 지뢰있는 칸
point = []

for r in range(n):
    for c in range(n):
        if mine[r][c] == "*":
            point.append((r, c))



for r in range(n):
    for c in range(n):
        if board[r][c] == "x" and mine[r][c] == ".":
            board[r][c] = check(r, c)

        if board[r][c] == "x" and mine[r][c] == "*":
            for a, b in point:
                board[a][b] = "*"



for a in range(n):
    for b in range(n):
        print(board[a][b], end="")
    print()