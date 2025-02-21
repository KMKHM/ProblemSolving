"""
달팽이
문제: https://www.acmicpc.net/problem/1913
"""
import sys

input = sys.stdin.readline

n = int(input())

num = int(input())

board = [[0]*n for _ in range(n)]

# 이동 방향
dx, dy = (1, 0, -1, 0), (0, 1, 0, -1)

# 찾는 값
res = [0, 0]

# 방향
r = 1

# 초기 좌표
x, y = 0, 0

# 이동 수
m = n -1

while True:
    board[x][y] = n*n

    if n*n == 1:
        break

    # 아래
    for _ in range(m):
        x += dx[0]
        y += dy[0]
        board[x][y] = board[x-dx[0]][y-dy[0]] - 1

    # 오른쪽
    for _ in range(m):
        x += dx[1]
        y += dy[1]
        board[x][y] = board[x-dx[1]][y-dy[1]] - 1

    # 위쪽
    for _ in range(m):
        x += dx[2]
        y += dy[2]
        board[x][y] = board[x-dx[2]][y -dy[2]] - 1
    # 왼쪽
    for _ in range(m-1):
        x += dx[3]
        y += dy[3]
        board[x][y] = board[x-dx[3]][y-dy[3]] - 1

    n -= 2
    m -= 2
    x += 1


for i in range(len(board)):
    print(*board[i])

for i in range(len(board)):
    for j in range(len(board)):
        if board[i][j] == num:
            print(i+1, j+1)
            sys.exit(0)
