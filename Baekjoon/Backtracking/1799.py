"""
비숍
문제: https://www.acmicpc.net/problem/1799
"""
import sys

input = sys.stdin.readline

n = int(input())

board = [list(map(int, input().split())) for _ in range(n)]

# 정답
ans = 0

# 대각선 방향
dx, dy = (1, 1, -1, -1), (-1, 1, 1, -1)

# 대각선에 비숍을 놓을 수 있는지 판단하는 함수
def check1(a, b):
    for i in range(4):
        nx, ny = a, b
        while True:
            nx += dx[i]
            ny += dy[i]

            if not (0<=nx<n and 0<=ny<n):
                nx -= dx[i]
                ny -= dy[i]
                break

            if board[nx][ny] == "B":
                return False

    return True
def check2():
    pass

def bt(x, y):
    global ans

    if y == n-1:
        ans += 1
        return

    if x == n-1:
        bt(x+1, 0)
        return

    if board[x][y] == 1:
        if check1(x, y):
            board[x][y] = "B"
            bt(x, y+1)
            board[x][y] = 1
        else:
            bt(x, y+1)

    bt(x, y+1)

bt(0, 0)


print(ans)


